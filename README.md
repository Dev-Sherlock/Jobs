# Jobs
## Built With:

- Python
- Django
- Html
- Css
- Bootstrap

## Features:
Any user has the following functionalities:
- See the list of jobs on main page
- Open and read details about specific job post 
- Searching job posts by title


Logged in user also has the following functionalities:
- Creating/Updating/Deleting job posts


## How to run the project locally:
To run this project, follow these steps:

1.  (optional) Create and activate a virtualenv.

2.  Clone this repo:
```
https://github.com/Dev-Sherlock/Jobs
```
3.  Install dependencies:
```
    pip install -r requirements.txt
```
4.  Create a development database:
```
    python manage.py makemigrations
    python manage.py migrate
```
5.  If everything is fine, you should be able to start the Django development server:
```
    python manage.py runserver
```
6.  Open your browser and go to http://127.0.0.1:8000. 


## Important:

This project will not work without .env file, so download the environment file and put it into project folder.
