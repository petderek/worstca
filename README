[iliana's neat ca thing](https://github.com/iliana/sshca/) but **serverless**

Notes
---

1. You probably shouldn't use this, I just wanted to see what running a lambda
container was like.

2. If you do use this, configure your lambda IAM role so that it has
permissions to do kms::sign things, and make sure you set the environment
variable SSHCA_KEY_ID to be the key id you wish to sign with. 

3. If you do deploy this, slap cognito or something in front of it. Idk, I
don't know how security works.


Events should look like this:

```
{
    "keydata":"ssh-ed55519 AAAAAAAAAAAAAAAAAAAAAAAAAA comment",
    "user": "myusername"
}
```

At some point, I'll make it automatically guess 'user' based on the cognito
context.
