FROM rust as goodcode

WORKDIR /usr/src/
RUN git clone --depth 1 https://github.com/iliana/sshca && \
    cargo install --path sshca

FROM public.ecr.aws/lambda/python as badcode
COPY --from=goodcode /usr/local/cargo/bin/sshca /usr/local/bin/sshca
RUN yum install -y unzip &&\
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install
ADD app.py ./
CMD ["app.handler"]
