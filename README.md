# Electronic Senate Voting System
## Contributors
Group 7

| StudentId | StudentName                            | Email address                    |
| --------- | -------------------------------------- | -------------------------------- |
| A1776064  | Arun Kumar Rajasekar                   | a1776064@student.adelaide.edu.au |
| A1763100  | Harshini Subramani                     | a1763100@student.adelaide.edu.au |
| A1787719  | Rishi Kumar Ramaiya Srinivasan Kumaran | a1787719@student.adelaide.edu.au |
| A1778500  | Subramanian Kannan                     | a1778500@student.adelaide.edu.au |
| A1775044  | Varsita Narayanasamy                   | a1775044@student.adelaide.edu.au |

## Project description
Electronic senate voting application, the project to implement a secure and robust web based Voting application for Australian Senate by following the design paradigm, principles and by incorporating the key security elements such as authentication, authorization, audit, confidentiality, integrity and availability.

## Prerequisites
The tools required to run the code of our project are,
Firstly to install conda
The below link will direct to install anaconda3,
https://www.anaconda.com/distribution/
```
conda create --name eVotingEnv django
activate eVotingEnv (source activate eVotingEnv for Mac Users)
cd eVotingApp
```
For Database: 
My SQL is used for the current system,
The below link will direct to install ,
https://www.mysql.com/products/workbench/
```
create DATABASE evoting;
```
Also, install the following modules 
```
pip install bcrypt
pip install pillow
pip install django-widget-tweaks
```

## Run
To run the Electronic Senate Voting Application
```
python manage.py runserver
python manage.py migrate
python manage.py makemigrations authentication
```

