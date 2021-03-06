from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class QuestionManager(models.Manager):
    def new(self):
        return super(QuestionManager, self).order_by('-id')

    def popular(self):
        return super(QuestionManager, self).order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name="question_author", on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user', blank=True)

    objects = QuestionManager()

    class Meta:
        ordering = ('-added_at',)

    def get_url(self):
        return reverse('question', kwargs={'question_id': "/"+str(self.pk)})

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('added_at',)

    def get_url(self):
        return reverse('question', kwargs={'question_id': self.question.id})

    def __str__(self):
        return "Answer by {0} to question {1}: {2}...". \
            format(self.author.username, self.question.id, self.text[:50])
