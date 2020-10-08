# mpulse django coding challenge

## Set up the environment ##
Add the python3 versions of virtualenv and virtualenvwrapper to your machine if they are not already installed. [See this page for instructions](https://medium.com/@gitudaniel/installing-virtualenvwrapper-for-python3-ad3dfea7c717)
Create a new virtual environment for this project by opening a command window (terminal, command line environment of some sort) and entering 
~~~
mkvirtualenv mpulse
~~~
This will create a new virtual environment called 'mpulse'. Before beginning work on the project by opening the command window and activating the virtual environment by entering
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
The server should start with no stack traces or error messages.  You can test it by opening a browser on the same machine as the code is running on and navigating to http://localhost:8000/admin. You should see the Django administration dashboard. You should be able to administer Groups, Users and Members. Groups and Users are included by default in Django
## The Django Admin Dashboard ##
Once the web server is running, visit the Admin dashboard. The default admin user name and password are 'mpulse/mpulse'. In a browser, enter the admin dashboard URL:
~~~
http://localhost:8000/admin
~~~
The AUTHENTICATION AND AUTHORIZATION section is automatically generated. You can enter and edit new users. The MPULSEAPI section is the admin area for the API, which currently has only one table, Members. You can enter/edit members there. Note that 'Phone number' and 'Client member id' are both constrained to be unique for a given Account id.
Enter several new members.
## The GET endpoints ##
Test the GET endpoints either using a tool like curl or Postman or entering the endpoint URLs in a browser:
~~~
http://localhost:8000/member?account_id=<an account id>
http://localhost:8000/member?phone_umber=<a phone number>
http://localhost:8000/member?client_memmber_id=<a client member id>
~~~
Two endpoints are provided for accessing members by id:
~~~
http://localhost:8000/member?id=<an id #>
http://localhost:8000/members/<an id number>
~~~
## Create a new Member ##
Again, using your favorite tool POST a new member. The curl command is
~~~
>curl --user mpulse:mpulse -d 'first_name=Ralph&last_name=Mouse&account_id=1&phone_number=3235551234&client_member_id=42' -X localhost:8000/members/
~~~
The response should be a JSON blob showing the newly created data.
## Bulk Uploads ##
Bulk uploads of csv files has been implemented as a django management command. To perform a bulk upload, change to the directory containing manage.py and invoke like so: 
~~~
(mpulse)>python manage.py bulk_upload <fully qualified file name of csv file>
~~~
Uploaded data will print to the console. If data integrity constraints are violated (duplicate phone_number/account_id or client_member_id/account_id) an IntegrityError will be thrown and caught. In this implementation, the offending data will have to be corrected or removed by hand before the file upload can continue.
>python 
# WHAT HASN'T BEEN DONE #
My time is limited. The Django app is FAR from production-ready. 
1. Most eggregiously, I have not written any unit tests. Unit tests are an absolute necessity in a Python application as errors are not discovered until the erroneous code is invoked. Near-complete test coverage eliminates a host of nasty surprises. 
2. ~~GET and POST methods have been implemented. PUT and DELETE methods should also be implemented but were not requested.~~
3. Error handling is nearly non-existent. Production code should include comprehensive error handling.
4. Production code should be deployed to a production-strength web server, Apache, NGINX or the like. Production code SHOULD NOT be run on the development web server included in Django
5. The app is running against a sqlite database - something more substantial should be used in production: Oracle if you're rich, PostgreSQL or MySQL if not
6. There is no input checking - this is also an eggregious gap. The phone_number field should be validated. Non-validated input is a security vulnerability.
7. The Member object should have a last_modified field to keep track of updates.
8. I have not run the code through PyLint - the code falls far short of PEP8 compliance.
9. Bulk insertion is not fully implemented as an http endpoint, but rather as a custom manage.py command. See above for details
10. Logging should be implemented. 
