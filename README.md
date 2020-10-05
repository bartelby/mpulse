# mpulse django coding challenge

##Set up the environment##
Add the python3 versions of virtualenv and virtualenvwrapper to your machine if they are not already installed. [See this page for instructions](https://medium.com/@gitudaniel/installing-virtualenvwrapper-for-python3-ad3dfea7c717)
Create a new virtual environment for this project by opening a command window (terminal, command line environment of some sort) and entering 
~~~ mkvirtualenv mpulse ~~~
This will create a new virtual environment called 'mpulse. Before beginning work on the project by opening the command window and activating the virtual environment by entering
~~~ workon mpulse ~~~
You should now see "(mpulse)" immediately to the left of the command prompt. If so, we are ready to begin.
##Get the code##
In the command window, cd to your project directory and clone the mpulse project from my github repository like so
~~~(mpulse)>git clone git@github.com:bartelby/mpulse.git~~~
This should create and populate a directory called 'mpulse'
##Get the modules required for the project##
Run the following code to load the required modules into the virtual environment:
~~~(mpulse)>pip install -r requirements.txt

 
