# GoudaTime &middot; [![Available on Test Pilot](https://img.shields.io/badge/available_on-Test_Pilot-0996F8.svg)](https://goudatime.com/)[![CircleCI](https://circleci.com/gh/GFynbo/GoudaTime/tree/master.svg?style=svg)](https://circleci.com/gh/GFynbo/GoudaTime/tree/master)

GoudaTime is the Tinder of the restaurant industry. GoudaTime allows you and your friends to join a virtual party and vote yes or no on restaurants near you. If the entire party votes yes on any restaurant it will show up under your list of matches with information pertaining to the restaurant. We're here to make sure you all get something you want to eat!

---

## Tasks & Goals
### TODOS
* [ ] Potentially get a animation like a spinning wheel for the loading of the map
* [ ] Allow uses to add a profile picture (not sure if I want to allow this)
* [ ] Move forms into individual files in one folder
* [x] ~~Re-organize the models AND forms into individual files for aesthetics and styles~~
* [x] ~~Center login/signup buttons on the nav bar~~
* [x] ~~Show active page on the navbar~~
* [x] ~~Remove 'Deny' model and implement single field in Match to determine whether its a match or deny~~
* [x] ~~Allow users to update and edit their existing profiles~~
* [x] ~~Add delete feature on existing matches~~
* [x] ~~Switch to postgresql from sqlite3~~
* [x] ~~**Fix styling to allow google maps to be the background on the index page**~~ <--- idea removed
* [x] ~~Force matches into all being the same size (picture, text, height, width etc) and center~~
* [x] ~~Get user's current location and update their profile/model instance <--- IMPORTANT~~
* [x] ~~Trigger button disable on 'get current location' feature of the update location~~

### BIG TODOS
* [ ] **Dynamically load restaurants from surrounding area**
    * [x] ~~Google maps implemented but need to use current (geolocation) to get and store the data into the user models~~
    * [x] ~~Also need to convert latitude and longitude to street address to allow the user to better understand where they are~~
* [ ] Allow group matching to help people decide on a place to eat together

---

## Local development

### Requirements
* Python 3
* pip
* postgresql or sqlite (if you get sqlite you need to change the data schema see step 6)
* a hardworking attitude!

To run this project in your development machine, follow these steps:

1. (optional) Create and activate a virtualenv (you may want to use virtualenvwrapper).

2. Ensure that the executable pg_config is available on your machine. You can check this using which pg_config. If not, install the dependency with one of the following.

3. macOS: brew install postgresql using Homebrew
3.1. Ubuntu: sudo apt-get install libpq-dev

4. Fork this repo and clone your fork:
~~~
git clone https://github.com/GFynbo/GoudaTime.git
~~~

5. Install dependencies:
~~~
pip install -r requirements.txt
~~~

6. Create a .env file under the /GoudaTime/ folder (inside the project folder i.e. GoudaTime/GoudaTime/) that contains the environment variables including the REQUIRED google maps api key!!
    ~~~
    SECRET_KEY='SECRET_KEY_HERE'
    DATABASE_PASSWORD='DATABASE_PASSWORD_HERE'
    MAPS_KEY='GOOGLE_MAPS_JAVASCRIPT_API_KEY_HERE'
    ~~~

    1. Either keep the existing postgresql schema for the database or switch to a local sqlite3 which can be done by chanding the settings from

    ~~~
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'DATABASE_NAME',
            'USER': 'USERNAME',
            'PASSWORD': DATABASE_PASSWORD,
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ~~~

    To

    ~~~
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }
    ~~~

7. Create a development database:
~~~
./manage.py migrate
~~~

8. If everything is alright, you should be able to start the Django development server:
~~~
./manage.py runserver
~~~

9. Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.

---

## The Team

[Gavin Fynbo](https://gavinfynbo.com) (Development Lead), [Tatiana Diaz-Gallegos](https://tatianaodg.com) (Developer), [Jio Jung](https://github.com/jungjio) (Developer)
