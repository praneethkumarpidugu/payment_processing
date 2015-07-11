##Payment Processing

##Features

- [x] Create Payment Processing
- [x] Manage users Data
- [x] Add and Modify fields in both admin and user side.

##Development Setup

```shell
git@github.com:YOUR_USER_NAME/payment_processing.git
cd payment_processing
```
#Make sure you have virtualenv installed if not follow the below instructions

```shell
pip install virtualenv
```
#Below are the steps to activate the virtualenvironment to create safest dist-packages which wont affect your system-libraries

```shell
virtualenv venv
source venv/bin/activate
```

#Below are the steps to install the dependency packages for this project
##Payment Processing relies on the Django Web Framework and hence we need to install the django package
##If you are used to apt-get or pip you can proceed with any of the methods

```shell
pip install django==1.7.2
```

#This project has already performed makemigrations so you dont need to do this step. Directly populate the data
#using migrate and createsuperuser for your admin privileges

```shell
python manage.py migrate
python manage.py createsuperuser

#Run the API

```shell
python manage.py runserver
```

Your production backend environment will be available in [127.0.0.1:8000/admin](127.0.0.1:8000/admin)