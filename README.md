# Open_project_10

# Project Openclassroom : Créez une API sécurisée RESTful en utilisant Django REST
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)  [![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](http://forthebadge.com).

Ce projet est une api de gestion de projet qui permet d'ajouter a la maniere d'une api des projets, commentaires et de participants

### library and tools

- https://www.djangoproject.com/ Django
- https://pypi.org/project/Pillow/ Pillow
- https://www.django-rest-framework.org/ Rest Framework


### Prerequisites

You should have Python on you're OS and set a Venv before continue if you want to have a clean env

you have to install the requirements with the command ``pip3 install -r requirements.txt``


## Launching

Once the project is well configured, execute the command ``python3 manage.py makemigrations`` then ``python3 manage.py migrate`` in order to install the database.

If you want to launch the project to be able to browse the site, run the command ``python3 manage.py runserver``


## Functional

This project aims to allow users to be able to request or create book reviews, and also to be able to browse them in order to collect opinions on specific books that may or may not exist in the site's library.

The user must be logged in to be able to perform all the following actions, or even to browse them

Each user can create a Ticket, ie a book, and he can publish at the same time the review of the book directly
They can also ask for reviews of a book thanks to the action "ask a review" in this case each person who sees their post will be able to publish a review.
And they can, as said just above, respond to a request for a book review.

The user's home page feed will display posts from the user and people they follow.

To subscribe to someone just go to the author's page and subscribe to the one he wants.
And then on this subscription page he can manage these subscriptions and see these subscribers

## Postman Documentation


Here you will have the documentation of the setting you will have to set for use postman with this api
- https://documenter.getpostman.com/view/19733343/2s93ebTWFc

## Made with

* [Visual Studio Code](https://code.visualstudio.com/) - Code editor


## Author

* **Hadrien Louppe Herbet** _alias_ [@herbetelem](https://github.com/herbetelem)
