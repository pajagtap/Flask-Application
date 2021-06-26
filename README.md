# Flask Application



### Introduction
In this application, we are going to build a simple REST API using Flask in Python, data will be read from CSV file and then user can make request as per the need. 

Apart from this, we are also going to have that rest api dockerized and deployed using docker. We will create docker image, container and then deploy the same. For more details about docker please follow this link, [Docker Info](https://docs.docker.com/compose/gettingstarted/) and also you simply download the docker using this [Docker Download](https://www.docker.com/products/docker-desktop)

Api will be running on localhost with port 5000 and then we can perform the rest operations using Postman tool. Here, is the link to download [Postman Download](https://www.postman.com/downloads/). You can google about Postman, basically its a tool used for making GET/POST/DELETE/PUT request for rest api consumption. 


##### Problem Statement
We have a CSV file named "books-2.csv". It contains the details for various books, their authors, genre, price and other attributes related information. We will be reading that CSV file and then return the required data back to flask application. We will be using Flask-Restful for this application. 


##### ...
If you want to run the application on your system, just use the 
```bash
git clone <repository>
```
To get all the files on your system. Then install all the required modules using requirements.txt. 
Once the modules are installed, you can go to the folder using following cmd commands and run the application as,
```bash
$ cd <folder_path>

$ python app.py
```

The app will run on the localhost and then you can use Postman application to make requests.
1. Request Type I
https://127.0.0.1:5000/books
This request needs input in json format as { "rows":3}. Once you make GET request using the proper json input, in the response you will be able to see the information for mentioned number of books (rows identifies the number of books to be retrieved.).

2. Request Type II
https://127.0.0.1:5000/books
This request will give freedom to the user to filter and see any data from the file. The user could only able to filter from the given column list. If a column is not present then a graceful error message should return. Even if the API didn’t find any filter response then the user should get a empty response.


Once the api is build, we can dockerize it and deploy it so that to access from remote servers. For that, you will need to have docker installed on the system and account on docker hub. Then you can follow steps as below,
To check docker version
```bash
docker --version

docker info
```

For dockerization, you will need to create a dockerfile which will be then fetched to create a docker image using commands in it. For simplicity, I have already uploaded one. When you clone the repository it will be downloaded with the same. After that follow the steps as,

```bash

// build the docker image
docker build -t application .


// list out the docker images
docker images


// login to your docker hub
docker login

// tag the image using the repository name
docker tag application <repository_name>/<username>:<tag_name>


// push the docker images
docker push <repository_name>/<username>:<tag_name>
```

After this step, you can check if the image is been uploaded to your docker hub.
Then will run the container using,
```bash

// run the docker container
docker run -d -p 5000:5000 --name <tag_name> application

// list the containers
docker ps -a

// check the docker logs
docker logs application

// execute the application into running container
docker exec -it application /bin/sh

// to stop
docker stop <container_id>
```
**For dockerization, it is supposed that you will have basic knowledge on the same.
