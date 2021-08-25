# README

==========
Code Style
==========

`PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_

==============
Requirements
==============

1. Django (1.11)
2. Django REST Framework (3.7)
3. mysqlclient (1.3.12)

===============
Getting Started
===============

**Installation**

After obtaining this repo, I advise that you create a `virtenv <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_
in the repository root. Following this you can install local requirements with the following
command::

    $ pip install -r requirements/local.txt 

You will also need to have Python 3.5 or 3.6 and MySQL already installed on your machine.

|

**Setting Virtual Environment Variables**

From the repo root, navigate to settings folder::

    $ cd tact_api/config/settings

Notice the following function defined in base.py ::

    def get_env_variable(var_name):
    """Get the environment variable or return exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)

The **get_env_variable** function is used in both **base.py** and **local.py** to obtain virtenv variables::

    SECRET_KEY = get_env_variable('SECRET_KEY')

    'USER': get_env_variable('DB_USER'),
    'PASSWORD': get_env_variable('DB_PASS'),
    'PORT': get_env_variable('DB_PORT'),

Navigate to your virtenv folder from the repo root::

    $ cd virtualenv/bin

In the **activate** file set your virtenv variables similar to::

    # Secret Key
    export SECRET_KEY='<ENTER YOUR SECRET KEY HERE>'

    # Database
    export DB_USER='ENTER DATABASE USER HERE'
    export DB_PASS='ENTER DATABASE PASSWORD HERE'
    export DB_PORT='ENTER PORT NUMBER HERE'

Please remember to leave your virtenv out of version control. This otherwise defeats the purpose
of setting virtenv variables!

|

**Initialize Database, Setup Users**

Now we can initialize your database. From the **tact_api** folder run::

    python manage.py makemigrations --settings=config.settings.local

Then run::

    python manage.py migrate --settings=config.settings.local

Create an admin user as follows::

    python manage.py createsuperuser --settings=config.settings.local

Finally, you can start the local server with::

    python manage.py runserver --settings=config.settings.local

Open a web browser and nagivate to http://127.0.0.1:8000/ to interact with the API in HTML mode.

===========
Contribute
===========

I welcome any contributions in identify bugs, implementing fixes, refactoring code or better 
documentation; whatever can help make this project a success! A contributing guideline will be
developed within short.

========
License
========

GNU GPLv3 @ Kenyatta M. Daniel









