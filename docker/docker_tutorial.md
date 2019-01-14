# Docker Tutorial
Step by step docker command practice.

## Hello world
- `docker run hello-world`
- `docker ps -a`
- `docker rm [container ID]`
- `docker images`
- `docker rmi [Image ID]`

## Pull Ubuntu 16.04
- `vim hello_world  # save file`
- `docker run -it ubuntu:16.04 /bin/bash`
- `exit  # from container`
- `docker images`
- `docker ps -a`
- `docker logs [container ID]`
- `docker start -id [container ID]`
- `exit  # from container`
- `docker cp . [container ID]:/data/`
- `docker commit [container ID] my_ubuntu`

## Dockerfile
- `vim Dockerfile  # add commands below and save`
	```
	FROM ubuntu:16.04
	RUN echo "hello_world"
	COPY . /data/
	WORKDIR /data/
	```
- `docker build -t my_ubuntu_2 .`
- `docker images`
- `docker run -it my_ubuntu_2 /bin/bash`
- `exit`

Check customized Dockerfiles in this [repo](https://github.com/ufoym/deepo)

## Dockerhub(Pull)
Can download pushed docker images from [Dockerhub](https://hub.docker.com/)
- `docker run -it ros  # pull ros image`

## Dockerhub(Push)
1. Sign in [Dockerhub](https://hub.docker.com/)
2. Create repository
3. Check the Docker command: `docker push [docker ID]/[repository name]:tagname`
4. Change image name fit into the command template: `docker tag [image ID] [docker ID]/[repository name]:0.1`
5. `docker login`
6. `docker push [image ID]/[repository name]:0.1`
