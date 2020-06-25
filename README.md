# Overview
* A website that uses Django framework to implement basic Instagram functionalities
    * User registration/login/logout
    * Post CRUD operation
        * make/modify/delete a post
    * User timeline page
        * shows posts from users that current user is following 
    * User profile page
        * shows a user's all posts
    * User interactions
        * follow/un-follow
        * likes
        * comments
        
# Installation
## Install required modules
```pip install requirements.txt```
## Set up data models
```python manage.py makemigrations```
```python manage.py migrate```
## Create super user (optional)
```python manage.py createsuperuser```
## Run the server
### Quick way with built-in Django command
```python manage.py runserver```
### Comprehensive way with web server (NGINX or Apache HTTP server) and WSGI server (uWSGI or gunicorn)
**Why do we need NGINX and uWSGI?**
1. NGINX works as a reverse proxy to 1.serves static contents 2. directs dynamic request to WSGI server
2. uWSGI sits between NGINX and our Django web application, connects to NGINX via sockets and talks to web application via wsgi.py 
* NGINX
    * install NGINX
    * modify mysite_nginx.conf
        * change /static route to the static folder under your project
    * test NGINX with mysite_nginx.conf - ```nginx -t -c mysite_nginx.conf```
        * you might need to change http.include field to point to right mime file path if the system is not Mac
    * start NGINX server - ```nginx -c mysite_nginx.conf```
        * stop NGINX serve - ```nginx -s quit```
* uWSGI
    * install uWSGI - ```pip install uwsgi```
    * modify uWSGI config file uwsgi.ini (optional)
        * change pidfile and daemonize if needed
    * start WSGI server - ```uwsgi --ini uwsgi.ini```
        * run ```uwsgi --stop PID_FILE``` to stop the server, PID_FILE is configured in uwsgi.ini

# Access
Use 'http://127.0.0.1:8000/insta/posts/' to access the website and 'http://127.0.0.1:8000/admin' for admin management