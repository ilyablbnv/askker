from __future__ import unicode_literals

# from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone
from vote.managers import VotableManager


class Question(models.Model):
    topics = models.ManyToManyField('questions.Topic', related_name="questions")
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=200)
    author = models.ForeignKey(User, default="")
    slug = models.SlugField(default="")
    created_at = models.DateTimeField(default=timezone.now)
    votes = VotableManager()

    # Compute the nicely printable string representation of an object.
    def __str__(self):
        return self.title

    # Calculate the URL for an object. Return a string, which can be used to refer to the object over HTTP
    def get_absolute_url(self):
        return reverse("question", kwargs={"pk": self.id})

    def votes_count(self):
        return self.votes_count()


class Topic(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey("questions.Question", related_name="answers")
    author = models.ForeignKey(User, default="")
    text = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)

