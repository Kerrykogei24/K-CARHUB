# CARHUB

[Kerry Komar](https://github.com/Kerrykogei24/K-CARHUB)  
  
# Description  
The project enables users post cars pieces from their hood and other users can comment on the piece and even follow and subscribe to get newsletter about the web app


##  Live Link  
 Click [View Site](https://carhub24.herokuapp.com/photos)  to visit the site
  

## User Story  
  
* A user can view different posts posted by other car dealers
* A user can post their cars pieces
* A user can comment on cars pieces and even follow other car dealers 
* User can see description of a single cars  
* A user can subscribe to the newsletter
* A user can create their own profile and log in to the webapp
* A user can view their profile page. 
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
```bash
https://github.com/Kerrykogei24/K-CARHUB
```
##### Navigate into the folder and install requirements  
 ```bash
 cd CARHUB pip install -r requirements.txt 
 ```
##### Install and activate Virtual  
```bash
- python3 -m venv virtual - source virtual/bin/activate
```
##### Install Dependencies  
```bash
 pip install -r requirements.txt 
``` 
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations carhubapp
 ``` 
 Now Migrate

```bash
python manage.py migrate 
```
##### Run the application  
```bash
python manage.py runserver 
```
##### Testing the application  
```bash
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
 
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 3.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [kerrykomar@gmail.co]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/Kerrykogei24/K-CARHUB)  
* Copyright (c) 2021 **Kerry Komar**