=============================
django-template-obfuscator
=============================

.. image:: https://badge.fury.io/py/django-template-obfuscator.svg
    :target: https://badge.fury.io/py/django-template-obfuscator

.. image:: https://travis-ci.org/rafahuelin/django-template-obfuscator.svg?branch=master
    :target: https://travis-ci.org/rafahuelin/django-template-obfuscator

.. image:: https://codecov.io/gh/rafahuelin/django-template-obfuscator/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/rafahuelin/django-template-obfuscator

Obfuscates desired content in a Django template in order to be difficult to scrape

Documentation
-------------

The full documentation is at https://django-template-obfuscator.readthedocs.io.

Quickstart
----------

Install django-template-obfuscator::

    pip install django-template-obfuscator

Add it to your `INSTALLED_APPS`:

.. code-block:: django

    INSTALLED_APPS = (
        ...
        'django_template_obfuscator.apps.DjangoTemplateObfuscatorConfig',
        ...
    )

How to use django-template-obfuscator's template tags:
------------------------------------------------------

.. code-block:: django

    {% load static %}
    {% load obfuscator %}

    <!-- Place text to encode in between the {% obfuscate %} and {% endobfuscate %} template
    tags, then embed it into an Html element with the "obfuscated" class, that will will be
    "deobfuscated" using Javascript  -->

    <!-- CSS file that will avoid the user to copy the content in obfuscated class -->
    <link rel="stylesheet" href="{% static 'css/django_template_obfuscator.css' %}">

    <p class="obfuscated">
        {% obfuscate %}
        Text difficult to scrape.
        {% endobfuscate %}
    </p>

    <p class="obfuscated">
        {% obfuscate %}
        This text as well.
        {% endobfuscate %}
    </p>

    <!-- JS in charge of deobfuscation, making the content understandable to the web's user -->
    <script src="{% static 'js/django_template_obfuscator.js' %}"></script>

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install selenium
    (myenv) $ python django_template_obfuscator/tests.py


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
