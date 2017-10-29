# GoudaTime
***

The tinder of resaurants!

## Local development

To run this project in your development machine, follow these steps:

1. (optional) Create and activate a virtualenv (you may want to use virtualenvwrapper).

2. Ensure that the executable pg_config is available on your machine. You can check this using which pg_config. If not, install the dependency with one of the following.

3. macOS: brew install postgresql using Homebrew
3.1. Ubuntu: sudo apt-get install libpq-dev

4. Fork this repo and clone your fork:
~~~
git clone https://github.com/openshift/django-ex.git
~~~

5. Install dependencies:
~~~
pip install -r requirements.txt
~~~

6. Create a development database:
~~~
./manage.py migrate
~~~

7. If everything is alright, you should be able to start the Django development server:
~~~
./manage.py runserver
~~~

8. Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.
