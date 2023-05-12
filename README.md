# Open_project_10

# Project Openclassroom : Créez une API sécurisée RESTful en utilisant Django REST
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)  [![forthebadge](https://forthebadge.com/images/badges/built-by-developers.svg)](http://forthebadge.com).

This project is an API to manage some project

### library and tools

- https://www.djangoproject.com/ Django
- https://pypi.org/project/Pillow/ Pillow
- https://www.django-rest-framework.org/ Rest Framework


### Prerequisites

You should have Python on you're OS and set a Venv before continue if you want to have a clean env

You have to install the requirements with the command ``pip3 install -r requirements.txt``

You should have Postman on you're OS and set with the param in this documentation
- https://documenter.getpostman.com/view/19733343/2s93ebTWFc
Or you can use other Software like the plugin in VSCode who can do the same than Postman


## Launching

Once the project is well configured, execute the command ``python3 manage.py makemigrations`` then ``python3 manage.py migrate`` in order to install the database.

If you want to launch the project to be able to browse the site, run the command ``python3 manage.py runserver``


## Functional

This project aims to create projects and then be able to assign project contributors with different roles. You will be able to create issues for each project based on your rights and leave comments on each issue, also based on your rights.

Each action follows the CRUD principle, meaning that if you have permission, you can create, modify, edit, and delete each element.


## Made with

* [Visual Studio Code](https://code.visualstudio.com/) - Code editor


## Author

* **Hadrien Louppe Herbet** _alias_ [@herbetelem](https://github.com/herbetelem)
