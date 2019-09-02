=====
Usage
=====

To use django-template-obfuscator in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_template_obfuscator.apps.DjangoTemplateObfuscatorConfig',
        ...
    )

Add django-template-obfuscator's URL patterns:

.. code-block:: python

    from django_template_obfuscator import urls as django_template_obfuscator_urls


    urlpatterns = [
        ...
        url(r'^', include(django_template_obfuscator_urls)),
        ...
    ]
