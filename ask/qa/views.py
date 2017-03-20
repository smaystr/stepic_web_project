# from django.shortcuts import render
from django.http import HttpResponse


def index(request, *args, **kwargs):
    return HttpResponse('index - OK')


def user_login(request, *args, **kwargs):
    return HttpResponse('user_login - OK')


def user_logout(request, *args, **kwargs):
    return HttpResponse('user_logout - OK')


def user_signup(request, *args, **kwargs):
    return HttpResponse('user_signup - OK')


def question(request, *args, **kwargs):
    return HttpResponse('question - OK')


def ask(request, *args, **kwargs):
    return HttpResponse('ask - OK')


def answer(request, *args, **kwargs):
    return HttpResponse('answer - OK')


def popular(request, *args, **kwargs):
    return HttpResponse('popular - OK')


def test(request, *args, **kwargs):
    return HttpResponse('OK')
