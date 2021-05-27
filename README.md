# ML-Model-inside-Docker-
Running a Linear Regression ML model inside a docker 
Step 1:- Check if docker is installed or not.
rpm -q docker-ce


Step 2:- Start Docker services.

systemctl start docker 


Step 3:- Pull the Centos Image from Docker hub.

docker pull centos:latest


Step 4:- Create a Container with the help of Centos image.

docker run -it --name MyOS centos:latest

Step 5:- New docker container has started.



Step 6:- Download Python3 softwere inside Container.
yum install python3

Step 7:-  Install all the libararies your Machine Learning model depends on.

pip3 install numpy
 
pip3 install sklearn

pip3 install pandas


Step 08 : Copy Your Dataset inside Docker.


docker cp dataset_filename(in your local system) docker_os_name:path 

Dataset copied sucessfully.
Step 9:-  Train your Model

Model trained sucessfully
Step 10:- Run your model

Our Model is sucessfuly running inside a docker container.
