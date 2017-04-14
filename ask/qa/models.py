import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class QuestionManager(models.Manager):
    def new(self):      # get_ +
        return super(QuestionManager, self).get_queryset().all().filter(pub_date__gte=datetime.date.today())

    def rating(self):   # get_ +
        return super(QuestionManager, self).get_queryset().all().filter(rating__gte=0)


class Question(models.Model):
    objects = QuestionManager()

    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')

    def get_url(self):
        return reverse('question', kwargs={'question_id': self.pk})

    def __str__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('question', kwargs={'question_id': self.question.id})

    def __str__(self):
        return "Answer by {0} to question {1}: {2}...". \
            format(self.author.username, self.question.id, self.text[:50])
