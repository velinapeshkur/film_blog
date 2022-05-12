# film_blog

This website is deployed at http://velinap.pythonanywhere.com/. You can navigate it there or run the project locally to test some admin features,
such as: 
- creating, editing and deleting a post
- accessing the drafts list
- approving or deleting comments

## Setup

Clone the repository:
```sh
$ git clone https://github.com/velinapeshkur/film_blog.git
$ cd film_blog
```

Create a virtual environment to install dependencies in and activate it:
```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Install the dependencies:
```sh
(env)$ pip install -r requirements.txt
```

Generate a Django Secret Key at https://djecrety.ir/

Create .env file for handling environment variables:
```sh
(env)$ echo SECRET_KEY='your_token' > .env
(env)$ echo DEBUG=False >> .env
```
Run the server locally:
```sh
(env)$ python manage.py runserver
```

Navigate to http://127.0.0.1:8000/

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
