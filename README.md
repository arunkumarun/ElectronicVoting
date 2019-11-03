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
Electronic senate voting application, the project to implement a secure and robust web based Voting application for Australian Senate by following the design paradigm, principes and by incorporating the key security elements such as authentication, authorization, audit, confidentiality, and integrity.

## Prerequisites
The tools required to run the code of our project are,
Firstly to install conda
The below link will direct to install anaconda3,
https://www.anaconda.com/distribution/
```
conda create --name eVotingEnv django
activate eVotingEnv (source activate eVotingEnv for Mac Users)
cd eVotingApp
python manage.py migrate
python manage.py makemigrations authentication
pip install bcrypt
pip install pillow
pip install django-widget-tweaks
```

## Run
To run the Electronic Senate Voting Application
```
python manage.py runserver
```
