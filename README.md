# SWE466
A website builds for Software engineering project management project  (Tasks with resources project).

## Prerequisites
- Python 3.8
- PostgreSQL >= 12

## Instructions

1. Install pipenv using pip:
```bash
pip install pipenv
```
2. Enter pipenv shell:
```bash
pipenv shell
```
3. Install dependencies in the virtual environment: 
```bash
pipenv install
```
4. Run the migrations: 
```bash
python manage.py migrate
```
5. Run the server: 
```bash
python manage.py runserver
```

## Instructions to contribute to the project:
1-Clone the project 
```bash
git clone https://github.com/Saif-Alotaibe/SWE466.git
```
1,2-If you already have copy from the project, run this command to fetch and merge last changes in the project to your copy:
```bash
git pull origin main
```

2-Go to project folder:
```bash
cd SWE466
```
3-Open new branch:
```bash
git checkout -b Yourbranchname
```
4-Make sure you are in Yourbranchname:
```bash
git branch
```
5-Do your changes to the project then make smaller commits for each change, example:
```bash
git add [Only Single file or smaller changes for multiple files]
git commit -m "a message represent what you do, ex: add function xx " 
```
6-Push you changes to Yourbranchname:
```bash
git push oirign Yourbranchname
```
7-Open Pull request through Github from Yourbranchname to main branch

8-Make sure no conflicts before merge and merge your branch to main branch.
