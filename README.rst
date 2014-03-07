Django Roadmap 
==============

TODO: Describe app


Installation
------------

Prerequisites:

* Django
* django-cms 4 (beta)
* django-hvad

If you want to install the latest stable release from PyPi::

    $ pip install django-roadmap

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-roadmap.git#egg=roadmap

Add ``roadmap`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'roadmap',
    )

Run the South migrations::

    ./manage.py migrate roadmap


Usage
-----

TODO: Describe usage


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
