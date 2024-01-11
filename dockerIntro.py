"""
OS: any operating system has two parts:
    1- kernal the part which interacts with hardware.
    2- application layer the part which installs applications on it or interacts with apps
    
VM or virtual machines: make an image of an OS and run it on another OS, so when you
install a VM on your machine you install the kernal and application layer of an OS, virtually on your computer

Docker: docker creates the application layer fully functional and it uses the kernal
of the operating system that is installed on your computer.

image:
    A Docker image is a file used to execute code in a Docker container.
    Docker images act as a set of instructions to build a Docker container,
    like a template. 
    A Docker image has everything needed to run a containerized application,
    including code, config files, environment variables, libraries and runtimes.
containers: are running images, so its an application which is run based on its image template.

installing docker on windows, prerequisites:
    1- you need to have wsl installed on your machine.
    2- go to turn windwos features on/off
    3- check Virtual machine platform
    4- check windows subsystem for linux
then install the docker, after a reboot of your machine.

now once your docker is installed you can open the cmd or docker cli.

# to download an image named whalesay from the dockerhub, following is the command
--docker pull docker/whalesay

#to download if the image does not exist and run it afterwards, and pass the hello-world to it. run it in wsl command not cmd
-- sudo docker run docker/whalesay cowsay hello-world!

Here's a breakdown of the above command:

    sudo: This is a Linux command that allows you to run the following command with superuser (root) privileges. 
    This may be required because Docker typically requires administrative privileges to run containers.
    
    docker: This is the Docker command-line tool, used for interacting with the Docker daemon.
    
    run: This is a Docker subcommand used to run a container from an image.
    
    docker/whalesay: This is the name of the Docker image. Docker images are typically hosted on Docker Hub, 
    and "docker/whalesay" is a playful example image that displays an ASCII art whale with a message. 
    When you run this image, it will display a message in a speech bubble coming from the whale.
    
    cowsay: This is a command-line utility often used in Unix-based systems to display a message using an ASCII
    art cow or other animals. In this case, the "cowsay" command is used inside the container to display a message.
    
    hello-world!: This is the argument passed to the "cowsay" command. It's the message that the ASCII art
    whale will "say" when the container is run.

docker commands:
    docker run:
        Usage: docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
        Explanation: This command is used to create and start a new container based on the specified image. 
        You can also provide optional options and override the default command if needed.
        -- docker run -d --name mywebapp -p 8080:80 nginx
        Command Explanation: This command starts a Docker container named "mywebapp" running the NGINX web 
        server image in the background. It maps port 8080 on the host to port 80 on the container.
    docker ps:
        Usage: docker ps [OPTIONS]
        Explanation: This command lists running containers. By default, it shows only the active containers. 
        Use the -a option to list all containers, including stopped ones.
        -- docker ps
        Explanation: This command lists currently running containers and provides details about them, 
        including the container ID, image name, ports, and status.
    docker images:
        Usage: docker images [OPTIONS]
        Explanation: This command lists all the available Docker images on your system. It shows details like image ID,
        repository, tag, and size.
        -- docker images
        Explanation: This command lists all the Docker images available on your system, 
        showing details such as the repository, tag, and size.
    docker build:
        Usage: docker build [OPTIONS] PATH | URL | -
        Explanation: Use this command to build a Docker image from a Dockerfile. 
        You specify the build context (usually the directory containing the Dockerfile) and optional build options.
        --docker build -t myappimage ./myapp
        Explanation: This command builds a Docker image named "myappimage" from a Dockerfile located in the "myapp"
        directory. The -t flag is used to specify the image name and optional tag.
    docker stop:
        Usage: docker stop [OPTIONS] CONTAINER [CONTAINER...]
        Explanation: This command stops one or more running containers. You can specify the container ID or name.
        --docker stop mywebapp
        Explanation: This command stops the container named "mywebapp." The container can be started again with docker start.
    docker start:
        Usage: docker start [OPTIONS] CONTAINER [CONTAINER...]
        explanation: Use this command to start one or more stopped containers. It's the counterpart to docker stop.
        --docker start mywebapp
        Explanation: This command starts the previously stopped "mywebapp" container.
    docker exec:
        Usage: docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
        Explanation: This command allows you to execute a command within a running container. 
        It's useful for running one-off tasks or debugging.
        -- docker exec -it mywebapp sh
        This command opens an interactive shell session (sh) inside the "mywebapp" container.
    docker pull:
        Usage: docker pull [OPTIONS] NAME[:TAG|@DIGEST]
        Explanation: You can use this command to pull an image from a registry (e.g., Docker Hub) to your local system.
        --docker pull ubuntu:20.04
        This command pulls the Ubuntu 20.04 image from Docker Hub to your local system.
    docker logs:
        Usage: docker logs [OPTIONS] CONTAINER
        Explanation: To view the logs of a specific container, use this command. It's helpful for troubleshooting and debugging.
        --docker logs mywebapp
        This command shows the logs of the "mywebapp" container.
    docker rm:
        Usage: docker rm [OPTIONS] CONTAINER [CONTAINER...]
        Explanation: This command removes one or more containers. You can specify container names or IDs. Be cautious as this is irreversible.
        --docker rm mywebapp
        This command removes the "mywebapp" container.
    docker rmi:
        Usage: docker rmi [OPTIONS] IMAGE [IMAGE...]
        Explanation: To remove one or more Docker images, use this command. Be cautious, as it's irreversible and will remove all tags for the specified image.
        --docker rmi myappimage
        This command removes the "myappimage" image.
    docker network ls:
        Usage: docker network ls [OPTIONS]
        Explanation: List all Docker networks. It provides information about network names, driver types, and their ID.
        --docker network ls
        Running this command will list all Docker networks on your system.
    docker volume ls:
        Usage: docker volume ls [OPTIONS]
        Explanation: List all Docker volumes. Volumes are used for data persistence. This command displays volume names, drivers, and their ID.
        --docker volume ls
        This command lists all Docker volumes on your system.
    docker-compose:
        Usage: docker-compose [OPTIONS] [COMMAND] [ARGS...]
        Explanation: This command is used for managing multi-container applications defined in a Compose file. It simplifies the orchestration of complex container setups.
        Example: You need a docker-compose.yml file to use docker-compose effectively. Here's a sample Compose file:
        --  yaml
            Copy code
            version: '3'
            services:
              web:
                image: nginx
              app:
                image: myappimage
        --
        This Compose file defines two services: "web" (using the NGINX image) and "app" (using the "myappimage" image).
        docker stats:
            Usage: docker stats [OPTIONS] [CONTAINER...]
        Explanation: This command provides real-time statistics about resource usage (CPU, memory, network, etc.) 
        for one or more containers.

        --docker stats mywebapp
        Running this command will show real-time resource usage statistics for the "mywebapp" container
        
delete all containers:
--docker container prune -f

Run a container with the nginx:1.14-alpine image and name it webapp:
--docker run --name webapp -d nginx:1.14-alpine


application. What is the base image used in the Dockerfile?
Inspect the Dockerfile in the webapp-color directory.
the command to do the above is to bring up the docker file of it and see whats inside
--cat webapp-color/Dockerfile

making an image for the above file:
    --docker build -t webapp-color ./webapp-color

You can run an instance of the "webapp-color" Docker image and publish port 8080 on the container to 
port 8282 on the host using the following docker run command:
--docker run -d -p 8282:8080 webapp-color

#run python that is downloaded
--docker run -it --rm python:3.6 /bin/bash

to open the dockerfile and change python to python:3.6-alpine
--nano webapp-color/Dockerfile

In the webapp-color directory, run the ls -l command to list the Dockerfile and other files.
Build a new smaller docker image by modifying the same Dockerfile and name it webapp-color and tag it lite.
--docker build -t webapp-color:lite

And modify Dockerfile to use python:3.6-alpine image and then build using docker build -t webapp-color:lite .

#remove a container
--docker rm whalesay
#remove image, first rm its running container
-- docker rmi whalesay
#to run a command on a running container do the following, cat the hosts content on whalesay
--docker exec whalesay cat /etc/hosts

#to know the color of ENV
--docker inspect whalesay
#go to this link to practice
https://kodekloud.com/topic/labs-environment-variables-3/


