## Overview
* A website that uses Django framework to implement basic Instagram functionalities
    * User registration/login/logout
    * Post CRUD operation
        * make/modify/delete a post
    * User timeline page
        * shows posts from users that current user is following 
    * User profile page
        * shows a user's all posts
    * User interactions
        * likes
        * comments
        
## Installation
### install required modules
```pip install requirements.txt```
### run Django migration
```python manage.py makemigrations```
```python manage.py migrate```
### create super user (optional)
```python manage.py createsuperuser```
### run the server
```python manage.py runserver```