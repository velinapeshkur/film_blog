# <img width="28" alt="Favicon" src="https://user-images.githubusercontent.com/94002579/168091088-fdc20c57-9338-4b09-8d1c-4efd3a2e85f3.png"> film_blog

FFFBlog is my personal portfolio website designed as a personal blog, made with **Python and Django** framework in the backend and **HTML, CSS and Bootstrap** for the frontend.


This project is hosted on http://velinap.pythonanywhere.com/. You can also run it locally to test some admin features, such as: 
- creating, editing and deleting posts
- accessing the draft list
- approving or deleting comments

## Setup

- Clone the repository:
```sh
$ git clone https://github.com/velinapeshkur/film_blog.git
$ cd film_blog
```

- Create a virtual environment to install dependencies in and activate it:
```sh
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

- Install the dependencies:
```sh
(venv)$ pip install -r requirements.txt
```

- Generate a Django Secret Key at https://djecrety.ir/

- Create .env file for handling environment variables:
```sh
(venv)$ cd blog_project
(venv)$ echo SECRET_KEY='your_token' > .env
(venv)$ echo DEBUG=True >> .env
```

- Make initial migrations: 
```sh
(venv)$ cd ..
(venv)$ python manage.py migrate
```

- Collect static files:
```sh
(venv)$ python manage.py collectstatic
```

- Create a superuser to access admin features:
```sh
(venv)$ python manage.py createsuperuser
```

- Run the server locally:
```sh
(venv)$ python manage.py runserver
```

- Navigate to http://127.0.0.1:8000/

## Screenshots

### Home Page
<img width="500" alt="Screenshot 2022-05-11 at 16 42 53" src="https://user-images.githubusercontent.com/94002579/167870812-58afdd10-58e3-4436-85d2-682c9c423e94.png">

### Create New Post
<img width="500" alt="Screenshot 2022-05-11 at 16 47 30" src="https://user-images.githubusercontent.com/94002579/167867526-3fc3c4d6-8186-49b5-a8ed-3903ef407560.png">

### Post View and Comment Section
Logged in:

<img width="500" alt="Screenshot 2022-05-11 at 16 44 01" src="https://user-images.githubusercontent.com/94002579/167871427-3f27a526-5502-46d7-8f1e-d86fa614ae75.png">

Logged out:

<img width="500" alt="Screenshot 2022-05-11 at 16 45 37" src="https://user-images.githubusercontent.com/94002579/167871960-67e2b2d3-9535-4b8b-9e41-306aa5e770e7.png">

### Drafts
<img width="500" alt="Screenshot 2022-05-11 at 17 00 06" src="https://user-images.githubusercontent.com/94002579/167868207-4f06a4a6-2925-4244-b597-194eb5cbc3fc.png">
