# build image
FROM registry.fiblab.net/general/dev:latest as builder
RUN mkdir /build
COPY . /build
WORKDIR /build
RUN ./scripts/init.sh 
RUN GOOS=linux go build -a -o comm_docker .

#generate clean, final image for end users
FROM ubuntu:20.04
COPY --from=builder /build/comm_docker .
RUN sed -i 's#http://archive.ubuntu.com/#http://mirrors.tuna.tsinghua.edu.cn/#' /etc/apt/sources.list

RUN apt-get update --fix-missing && apt-get install -y libproj-dev --fix-missing
#executable 
ENTRYPOINT [ "./comm_docker" ]

