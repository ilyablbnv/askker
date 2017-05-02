"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from questions.views.answer_create import AnswerCreateView

from questions.views.question_create import QuestionCreateView
from questions.views.question_list import QuestionListView
from questions.views.question_detail import QuestionDetailView
from questions.views.topic_detail import TopicDetailView

from project.views import login, auth_view, logout, register
from questions.views.vote_question import vote_question

urlpatterns = [
    # Question urls
    url(r'^$', QuestionListView.as_view(), name="index"),
    url(r'^question/(?P<question_slug>[\w-]+?)$', QuestionDetailView.as_view(), name="question_detail"),
    url(r'^question/(?P<question_slug>[\w-]+?)/answers/add$', AnswerCreateView.as_view(), name="answer_create"),
    url(r'^topics/(?P<topic_slug>[\w-]+?)$', TopicDetailView.as_view(), name="topic_detail"),
    url(r'^ask$', QuestionCreateView.as_view(), name="question_create"),

    # Auth urls
    url(r'^login/$', login, name="login"),
    url(r'^auth/$', auth_view, name="auth"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^register/$', register, name="register"),

    url(r'^admin/', admin.site.urls),

    # Vote url
    url(r'^vote/(?P<question_slug>[\w-]+?)$', vote_question, name='vote')
]
