# mpulse django coding challenge

## Set up the environment ##
Add the python3 versions of virtualenv and virtualenvwrapper to your machine if they are not already installed. [See this page for instructions](https://medium.com/@gitudaniel/installing-virtualenvwrapper-for-python3-ad3dfea7c717)
Create a new virtual environment for this project by opening a command window (terminal, command line environment of some sort) and entering 
~~~
mkvirtualenv mpulse
~~~
This will create a new virtual environment called 'mpulse. Before beginning work on the project by opening the command window and activating the virtual environment by entering
~~~
workon mpulse 
~~~
You should now see "(mpulse)" immediately to the left of the command prompt. 
Test that you are using a version of python >=3 by entering 
~~~
(mpulse)>python --version
~~~
The response should be some version of Python 3 or better. If so, we are ready to begin.
## Get the code ##
In the command window, cd to your project directory and clone the mpulse project from my github repository like so
~~~
(mpulse)>git clone git@github.com:bartelby/mpulse.git
~~~
This should create and populate a directory called 'mpulse'
## Get the modules required for the project ##
Run the following code to load the required modules into the virtual environment:
~~~
(mpulse)>pip install -r requirements.txt
~~~
## Initialize the database ##
First create the migration files. In the command window, run 
~~~
(mpulse)>python manage.py makemigrations
~~~
Then run 
~~~
(mpulse)>python manage.py migrate
~~~
## Start the server ##
To start the server in a test environment (DO NOT use for deployed code)
~~~
(mpulse)>python manage.py runserver
~~~
The server should start with no stack traces or error messages.  You can test it by opening a browser on the same machine as the code is running on and navigating to http://localhost:8000/admin. You should see the Django administration dashboard. You should be able to administer Groups, Users and Members. Groups and Users are included by default in Django. 
