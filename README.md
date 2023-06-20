# Project Title
**TechnicalDeptApp**, I named the project TechnicalDeptApp because I wanted to do something for my work and is also my exam project to get the certification from the Coding Factory 3 (educational program in software development) of the Athens University of Economics and Business https://codingfactory.aueb.gr/ so I combine them.

## Project Description
I made this app to store all the orders and repairs that we do at the technical department where I work. Users will have separate permissions depending on the type of work they do, now every repair and order will be user named so I know who did it (which is complicated now) and can communicate with them. It's an early version that I hope to develop even more in the future and add more actions and tools (like searching in lists).

## Technologies used
Python 3.11.3

Django 4.2.2

djangorestframework 3.14.0 (API)

drf-spectacular 0.26.2 (documentation)

Bootstrap 5.2 (front-end)


## INSTALLATION:
Download the app, open a terminal at the main folder of the project.

Create a virtual environment (need Python to be installed) and run:
```
python -m venv .venv
```
Activate the environment:
```
.venv\scripts\activate
```

Install the requirements:
```
pip install -r requirements.txt
```

Run the server:
```
python manage.py runserver 
```

Open a browser and go to:
http://127.0.0.1:8000/


## How to use the project
To use the app first of all you need a user, the app already have a database with users and data to test it. 

username: admin password: 1234

username: user1 password: 123qwe!@# (Note: he have some restrictions at supplier views)

username: user2 password: 123qwe!@#

username: user3 password: 123qwe!@# (Note: he have some restrictions at supplier views)


Or create a new database file but first delete the db.sqlite3 file from the folder of the app and on an activated enviroment run:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
After last command will ask you name, email (not necessary), password and again password

Now with the superuser you can login at the app http://127.0.0.1:8000/ or go to Django admin page http://127.0.0.1:8000/admin/ and work from there.

If you will start with an empty database before you add a order or repair you need first to add a new supplier or a new vehicle respectively. After that you create orders, repairs, suppliers, vehicles and new users, check different type of lists, details, you can edit or delete  records (for some actions need to be the author else you can't).

## Front-end (the views)
**All the lists that have property updated_at are descending ordered to show the new records first**

### Suppliers views
#### Suppliers list
Shows a table list with all the suppliers in the database.

**At the above view if you click the ID you will open the detail view:**
#### Supplier details 
Shows a table with all the detail of the selected supplier. Plus he have the edit and delete views of the selected supplier.
##### Edit view
Update the supplier.
NOTE: permission only to superusers/admins and orderers
##### Delete view
Delete the supplier.
NOTE: permission only to superusers/admins and orderers
#### New supplier
Create a new supplier.
NOTE: permission only to superusers/admins and orderers

### Order views
#### Orders list
Shows a table list with all the orders in the database.
#### Completed orders list
Shows a table list with the status of the order is Completed or Cancelled.
#### Incompleted orders list
Shows a table list with the status of the order is Waiting Offer or Awaiting Delivery or Incomplete.
#### My orders
Shows a table list with all the orders in the database of the logged in user.

**At all the above views if you click the ID you will open the detail view:**
#### Order details 
Shows a table with all the detail of the selected order. Plus he have the edit and delete views of the selected order.
##### Edit view
Update the order.
NOTE: permission only to the author
##### Delete view
Delete the order.
NOTE: permission only to the author
#### New order
Create a new order.

### Vehicles views
#### Vehicle list
Shows a table list with all the vehicles in the database.

**At the above view if you click the ID you will open the detail view:**
#### Vehicle details 
Shows a table with all the detail of the selected vehicle. Plus he have the repairs history, edit and delete views of the selected vehicle.
##### Repairs history view
Shows a table list with all the repairs that made at the vehicle.
##### Edit view
Update the vehicle.
##### Delete view
Delete the vehicle.
#### New supplier
Create a vehicle.

### Repairs views
#### Repairs list
Shows a table list with all the repairs in the database.
#### Completed repairs list
Shows a table list with the status of the repairs is Completed or Cancelled.
#### Incompleted repairs list
Shows a table list with the status of the repair is Waiting parts or Stand by or Incomplete.
#### My repairs
Shows a table list with all the repair in the database of the logged in user.

**At all the above views if you click the ID you will open the detail view:**
#### Order details 
Shows a table with all the detail of the selected repair. Plus he have the edit and delete views of the selected repair.
##### Edit view
Update the repair.
NOTE: permission only to the author
##### Delete view
Delete the repair.
NOTE: permission only to the author
#### New repair
Create a new repair.

### API's views
#### Suppliers API
The API for the Suppliers. CRUD all the authenticated users.
#### Orders API
The API for the Orders. Read and create all the authenticated users. Delete and update the authors
#### Vehicles API
The API for the Vehicles. CRUD all the authenticated users.
#### Repairs API
The API for the Repairs. Read and create all the authenticated users. Delete and update the authors
#### Users API
The API for the Repairs. Read and only for the superuser/admin.
#### ReDoc
API documentation
#### Swagger
API documentation
#### Download yaml file
Configuration file

### User views
#### Users
Shows a table list with all the users in the database.
#### Add user
Create a new user.
NOTE: permission only to superusers/admins.
#### Change password
Change password to the logged in user


## Back-end 

### Database
I used SQLite, is the default database that Djago use.

### The models
**CustomUser** I use an abstract user model of Django to add new custom fields and I do this for two reasons. First because we can't do it later (after the first migration). Second at this project is for permissions and for future updates/upgrates.

**Supplier**

**Order**

**Vehicle**

**Repair**

#### Abstract custom user
To user the custom user need to change a property at TechnicalDeptApp -> settings.py:
```
AUTH_USER_MODEL = "accounts.CustomUser"
```

### Views
Almost all the views are class based with custom changes like template use, queryset for filter ect, selected fields for view, setting the current user at the records and some permissions.

### 404 error:
To work the custom 404.html need to set at TechnicalDeptApp -> settings.py the DEBUG = False.

### Templates
Almost all the front-end views have seperate template only few of them use the same, in a future update I will try to merge them more. All of them extends the "base.html" and the list views include the "pagination.html" (same code).

### Permissions
User has is_technician, is_orderer and is_observer properties, they are for custom permissions, but I didn't use them in all templates, only in add, edit and delete supplier templates, to give access olny at superusers and buyers.
All the views have login required (exept the login views).
The edit and delete views of the Repairs and Orders can be accessed only from the authors of the record.
The new user can be accessed only from admins
API users can be accessed only from admins

### Pagination
All views are paginated to 5 records same for API views, that can be changed from views.py (separately for each app) for views change 
```
paginate_by = 5
```
and for the API's from settings.py find the following and change the "PAGE_SIZE" value.
```
REST_FRAMEWORK = { 
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5,
}
```

### Serializers
I used the Django REST framework to convert our models for the API views, we also used SlugRelatedField to avoid the problem where the serializer couldn't match the field that we wanted to match of the foreign key using the pk. Example we wanted the author = admin but it used the pk instead of the username.

### Test's
At the project I have some model tests and login urls tests (API and front-end).
The other views have a login_required decorator and the test's can't run, if the login_required decorator removed they work.

#### Runnig the tests
Activate the environment:
```
.venv\scripts\activate
```
Run the test:
```
python manage.py test
```

### Run on local network
Change at TechnicalDeptApp -> settings.py the bellow:
```
DEBUG = False
ALLOWED_HOSTS = ['*']
```

Then run server with:
```
python manage.py runserver [PC-ip]:8000 e.x: python manage.py runserver 192.168.1.2:8000
```
or
```
python manage.py runserver 0.0.0.0:8000
```
From another pc try to a browser [PC-ip]:8000 

## Future updates:
Better templates (some can be merged and/or used from more views).

Complete users managment from front-end (no edit user now).

Add user permissions to all the views/templates.

Searchable dropdown selections.

Searchable list.
