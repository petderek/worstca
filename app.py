import os
import subprocess
import tempfile

def handler(event, context):
    msg = {}
    
    if 'keydata' not in event:
        return "missing keydata element in event"

    if 'user' not in event:
        return "missing user in event"

    if 'SSHCA_KEY_ID' not in os.environ:
        return "missing SSHCA_KEY_ID in environment"

    with tempfile.TemporaryDirectory() as dirpath:
        isthisachroot = os.environ.copy()
        isthisachroot["HOME"] = dirpath
        os.mkdir(os.path.join(dirpath,".ssh")) 
        os.makedirs(os.path.join(dirpath,".config","sshca"))
        
        with open(os.path.join(dirpath,".config","sshca","env"), "w") as envfile:
            envfile.write("USER={}\nHOME={}".format(event['user'], dirpath))
           
        with open(os.path.join(dirpath,".ssh","id_ed25519.pub"), "w") as pubfile:
            pubfile.write(event['keydata'])
        
        task = subprocess.run(["/usr/local/bin/sshca", "sign"],capture_output=True, env=isthisachroot)
        msg['task'] = str(task)

        try:
            with open(os.path.join(dirpath,".ssh","id_ed25519-cert.pub")) as certfile:
                msg['signed'] = certfile.read()
        except:
            msg['error'] = "no certfile was written"

    return msg

