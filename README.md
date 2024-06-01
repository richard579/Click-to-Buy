# Click-to-Buy
# ALX Webstack Portfolio Project

-- Python, django and django REST framework for testing 

### This is the Backend repo for my Alx webstack porfolio final month project. The Backend is on development using python programming language using django and django REST frmawork for testing apis

## DESCRIPTION, AIMS AND OBJECTIVES

The **primary objective** of this project is to develop a user-friendly and comprehensive **"Online shopping system** software solution that can address the needs of shopping.

The solution covers:
	1. Shopping for basic needs on the go.
 
### Backend API for Online Store app!

### Tech & Tools

<img alt="Python" src="https://img.shields.io/badge/Python-blue?style=for-the-badge&logo=python&logoColor=FFD43B"/> <img alt="Django" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green"/>
<img alt="Django Rest" src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white"/> <img alt="PostgreSQL" src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img alt="Visual Studio Code" src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?&style=for-the-badge&logo=visual-studio-code&logoColor=white"/>

 As this will be the final portfolio project for our backend specialization, we'll focus majorly on the back end aspect.
 
## TEAM MEMBERS AND ROLE
Team members include
  1. Richard Bengtson
[Github](https://github.com/richard579)
richardbeng358@outlook.com

## CHALLENGES FACED

1. Scalability and Performance

2. User interface complexity

3. System inter-operations

4. Plan and context variations

5. Testing and Debugging

6. Project and scope management

7. User acceptance and adoption

## HOW TO RUN PLAN AND TEACH

### Clone Project
```sh
git clone 
```
```sh
cd Click-to-Buy--Backend
```

### Active environment and Install dependencies
```sh
pipenv shell
```
```sh
pipenv install
```
### Project Setup and Run

```sh
python manage.py makemigrations
```
```sh
python manage.py migrate
```

```sh
python manage.py seed_db
```

```sh
python manage.py runserver
```

### Run performance test

`locust -f locustfiles/browse_products.py`
