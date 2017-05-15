from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Question, Answer
from .forms import AskForm, AnswerForm, LoginForm, SignupForm
from django.http import HttpResponse


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


def answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            print('Answer is valid')
            form._user = request.user
            _answer = form.save()
            url = _answer.get_url()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect('/')


@require_GET
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
