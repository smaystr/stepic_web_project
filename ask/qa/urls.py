"""qa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login(/)?.*$', views.user_login, name='login'),
    url(r'^logout(/)?.*$', views.user_logout, name='logout'),
    url(r'^signup(/)?.*$', views.user_signup, name='signup'),
    url(r'^question(/)?(?P<question_id>[0-9]+)/$', views.question, name='question'),
    url(r'^ask(/)?.*$', views.ask, name='ask'),
    url(r'^answer(/)?.*$', views.answer, name='answer'),
    url(r'^popular(/)?.*$', views.popular, name='popular'),
    url(r'^new(/)?.*$', views.test, name='new'),
]
