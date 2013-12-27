dnd3.5-tools
============
Several tools for helping at Dungeon Masters (and players) during a session.

## Installation

1. Install pip & virtualenv if you don' have them and create a virtualenv.

2. Install mongodb and start it.

3. Clone the repo:
```
$ git clone https://github.com/maxicecilia/dnd3.5-tools
```
4. Install requeriments
```
$ pip install -r requirements.txt
```
5. Import some data if you want
```
$ mongoimport -d my_mongo_db -c character ../dumpdata/characters.json
```
6. Have fun!
```
$ python manage.py runserver
```

### Nitrous.io setup
If you wan to setup your application in Nitrous, this commands should help you:
```
$ parts install mongodb
$ parts start mongodb
$ virtualenv -p /usr/bin/python2.7 my_venv
$ source ~/my_venv/bin/activate
```

## Tech's Thoughts
This app was created to learn and test different things. This will use (or try):

* Django 1.6 + mongoengine (http://docs.mongoengine.org/en/latest/)
* MongoDB (as only database)
* Bootstrap 3
* Angular JS (someday...)
* Stylus (over the rainbow!)