# from django.shortcuts import render
from django.http import HttpResponse


def index(request, *args, **kwargs):
    return HttpResponse(
        content='OK',
        content_type='html/text',
        status=200,
    )


def user_login(request, *args, **kwargs):
    return HttpResponse(
        content='OK',
        content_type='html/text',
        status=200,
    )


def user_logout(request, *args, **kwargs):
    return HttpResponse(
        content='OK',
        content_type='html/text',
        status=200,
    )


def user_signup(request, *args, **kwargs):
    return HttpResponse(
        content='OK',
        content_type='html/text',
        status=200,
    )


def question(request, *args, **kwargs):
    return HttpResponse(
        content='OK',
        content_type='html/text',
        status=200,
    )


def ask(request, *args, **kwargs):
    return HttpResponse(
        content='OK',
        content_type='html/text',
        status=200,
    )


def answer(request, *args, **kwargs):
    return HttpResponse(
        content='OK',
        content_type='html/text',
        status=200,
    )


def popular(request, *args, **kwargs):
    return HttpResponse(
        content='OK',
        content_type='html/text',
        status=200,
    )


def test(request, *args, **kwargs):
    return HttpResponse(
        content='OK',
        content_type='html/text',
        status=200,
    )