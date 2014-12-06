ECIT Password Survey Application
==================

This application is written in [Flask](http://flask.pocoo.org);
"Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions."

Purpose
------------------
To survey and gather relevant user data on passwords and their usage.


Project Structure
------------------
####Application Project Structure
```
app
  ├── __init__.py
  ├── decorators.py
  ├── email.py
  ├── forms.py
  ├── mixins.py
  ├── models.py
  ├── static
  │   └── (asset files: CSS/JS/images)
  │       * managed 'mostly' by Bower
  ├── templates
  │   └── (HTML template files)
  └── views.py
config.py (not committed)
```

####Application Configuration
 * `config.py` - will hold all configuration values for the application runtime (sensitive data) **DO NOT COMMIT**.
 * `.bowerrc` - instructs bower to install files in the specified location
 * `bower.json` - the project's Bower configuration file


Getting Started
------------------

#####Installing Packaged Dependencies

You are strongly encouraged to use a virtual environment for development, and [virtualenv wrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) is the way to go.

Whether you use a virtualenv or not your first step is to install your Python dependencies:
 * with virtualenv wrapper
  * `$ mkvirtualenv survey_env -r requirements.txt`
 * without virtualenv wrapper
  * `$ pip install -r requirement.txt`

`requirements.txt` holds a record of all packaged Python dependencies. If you update or add any packages, please remember to run:
 * `$ pip freeze > requirements.txt`

#####Configuring/Initializing the Database

Configuration specifications will come in a later update. For now these are the config variables that will be utilized.
 * `SQLALCHEMY_DATABASE_URI`
 * `SQLALCHEMY_ECHO`
 * `SQLALCHEMY_RECORD_QUERIES`

To initialize the database, run:<br>
`$ python manage.py initdb`

Running the App
------------------

#####Development
To run the application in your development environment. After you initialize your database;
 * `$ python manage.py runserver`

The development server should start in `DEBUG` mode (this is specified in you config file) and with the reloader:
```
$ python manage.py runserver
* Running on http://127.0.0.1:5000/
* Restarting with reloader
```

#####Production

Documentation for this is coming soon.


Tools and Dependencies
------------------

All packaged Python dependencies can be found in `requirements.txt` and are managed using `pip`.

Most other packages (related to the application's front end) are managed with [Bower](http://bower.io/) and you can see this list in `bower.json`.

The style for the applications front end is based on Bootstrap but is customized by using a modified bootstrap swatch theme from [Bootswatch](http://bootswatch.com), namely 'Darkly'.

The custom style sheet is located in `app/static/bootswatch`.

We update styles by modifying the LESS files. These are compiled using [Grunt](http://gruntjs.com/):
```
$ grunt swatch:darkly
Running "swatch:darkly" (swatch) task
...
Done, without errors.
```


Contributors
------------------

[Ryan Kuhl](https://github.com/rkk09c)<br>
[Shiva Houshmand](https://github.com/shibba)<br>
[Frank Valcarcel](https://github.com/frankv)<br>