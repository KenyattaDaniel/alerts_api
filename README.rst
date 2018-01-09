# README

TacT JSON API
=============

.. image:: tact_project/logo.png
An API platform enabling professionals living in small developing countries to easily 
share and receive useful analysis, data and information.
**Tact API is currently under development**. Once completed, it will enable users to*;

* create and publish a timeline. 
* add events, tasks and news alerts to timelines
* subscribe to publicly available timelines
* provide feedback on timeline events, tasks & alerts

In the future Tact's API will power a mobile and web application. 

==========
Motivation
==========

I recently spent 7 years working on my home island of Sint Eustatius. As a young professional,
I saw first hand the challenges faced by local entrepreneurs, SME's and public organizations in 
accessing information and services needed to effectively run and growth their organizations. 
My experience inspired me to develop Tact; " the Bloomberg for island professionals!"  

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

    $ cd tact/settings

Notice the following function defined in base.py ::

    def get_env_variable(var_name):
    """Get the environment variable or return exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)

The **get_env_variable** is used in both **base.py** and **local.py** to obtain virtenv variables::

    SECRET_KEY = get_env_variable('SECRET_KEY')

    'USER': get_env_variable('DB_USER'),
    'PASSWORD': get_env_variable('DB_PASS'),
    'PORT': get_env_variable('DB_PORT'),

Assuming you have created a virtenv in the repo root, navigate to it as follows::

    $ cd virtualenv/bin

In the **activate** file set your virtenv variables similar to::

    # Secret Key
    export SECRET_KEY='<ENTER YOUR SECRET KEY HERE>'

    # Database
    export DB_USER='<ENTER DATABASE USER HERE>'
    export DB_PASS='<ENTER DATABASE PASSWORD HERE>'
    export DB_PORT='<ENTER PORT NUMBER HERE>'

Please remember to leave your virtenv out of version control. This otherwise defeats the purpose
of setting virtenv variables!

|

**Initialize Database, Setup Users**

Now we can initialize your database. From the repo root run::

    python manage.py makemigrations --settings=tact.settings.local

Then run::

    python manage.py migrate --settings=tact.settings.local

Create an admin user as follows::

    python manage.py createsuperuser --settings=tact.settings.local

Finally, you can start the local server with::

    python manage.py runserver --settings=tact.settings.local

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









