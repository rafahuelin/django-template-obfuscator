# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('django_template_obfuscator.urls', namespace='django_template_obfuscator')),
]
