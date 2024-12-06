# Simple Careers Crud in Django Rest Framework

After cloning this repository, use `cd` command to enter into the cloned repository  
```
cd careers-crud
```

## How to run this project
Install the required packages to run it with the below command:
```
pip install -r requirements.txt
```
The run the below commands to preapare the tables to be used for storing data
```
python manage.py makemigrations
python manage.py migrate
```

Then, execute the below command to start the server:
```
python manage.py runserver
```
To create a new item, send a post request to the url [localhost:8000/careers](http://localhost:8000/careers/) with a request body with the below fields  
```
{
    "username": "John",
    "title": "Lawyer",
    "content": "Hardworking layer"
}

```
To get all careers, make a get request to the endpoint [http://localhost:8000/careers/ ](http://localhost:8000/careers/)


To get a specific career, make a get request to http://localhost:8000/careers/1 where 1 is the id of an existing career stored in the database


To update a career, you must know its id and make a patch request to the url [http://localhost:8000/careers/1](http://localhost:8000/careers/1) where `1`is the id of an existing career  
and you must pass a json in the body with the items you want to update, like below:  
```
{
    "title": "Musician",
    "content": "A great artist"
}

```
You can only update the fields `title`and `content`.  
To delete an career, just make a delete request to url passing the id of the career you want to delete, like:
[http://localhost:8000/careers/4](http://localhost:8000/careers/4)
where 4 is the id of an existing career you want to delete.