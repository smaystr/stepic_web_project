# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import reverse
from .models import Question
from .forms import AskForm, AnswerForm, LoginForm, SignupForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@require_GET
def index(request, *args, **kwargs):
    question_list = Question.objects.new()
    paginator, page, limit = paginate(request, question_list)
    context = {
        'questions': page,
        'paginator': paginator,
        'limit': limit,
    }
    return render(request, 'qa/index.html', context)


def user_login(request, *args, **kwargs):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    form = LoginForm()
    return render(request, 'qa/login.html', {'form': form})


def user_logout(request, *args, **kwargs):
    if request.user is not None:
        logout(request)
        return HttpResponseRedirect(reverse('index'))


def user_signup(request, *args, **kwargs):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    form = SignupForm()
    return render(request, 'qa/signup.html', {'form': form})


def question(request, question_id):
    q = get_object_or_404(Question, id=question_id)
    answer_list = q.answer_set.all().order_by('-added_at')
    # paginator, page, limit = paginate(request, answer_list)
    form = AnswerForm(initial={'question': question_id})
    context = {
        'question': q,
        'answers': answer_list,
        'form': form,
        # 'paginator': paginator,
        # 'limit': limit,
    }
    return render(request, 'qa/question.html', context)


# @login_required
@csrf_exempt
def ask(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            _question = form.save()
            url = _question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


# @login_required
@csrf_exempt
def answer(request, *args, **kwargs):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            print('Answer is valid')
            form._user = request.user
            _answer = form.save()
            url = _answer.get_url()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect('/')


def popular(request, *args, **kwargs):
    # list of questions in desc order by rating
    question_list = Question.objects.popular()
    paginator, page, limit = paginate(request, question_list)
    context = {
        'questions': page,
        'paginator': paginator,
        'limit': limit,
    }
    return render(request, 'qa/popular.html', context)


def test(request, *args, **kwargs):
    return HttpResponse(
        content='OK',
        content_type='html/text',
        status=200,
    )


def paginate(request, lst):
    # get limit
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10

    # if limit is too high, normalize it
    if limit > 100:
        limit = 10

    paginator = Paginator(lst, limit)

    # get current page
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return paginator, page, limit
