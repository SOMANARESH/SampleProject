"""SampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.home),
    url(r'^topics/$', views.TopicsList.as_view()),
    url(r'^topics/(?P<pk>[0-9]+)/$', views.TopicsDetail.as_view()),
    url(r'^topics/numbers/$', views.NumberList.as_view()),
    url(r'^topics/numbers/(?P<pk>[0-9]+)/$', views.NumberDetail.as_view()),
    url(r'^topics/problems_on_ages/$', views.ProblemsOnAgesList.as_view()),
    url(r'^topics/problems_on_ages/(?P<pk>[0-9]+)/$', views.ProblemsOnAgesDetail.as_view()),
    url(r'^topics/progressions/$', views.ProgressionsList.as_view()),
    url(r'^topics/progressions/(?P<pk>[0-9]+)/$', views.ProgressionsDetail.as_view()),
    url(r'questions/$', views.QuestionsList.as_view()),
    url(r'questions/(?P<pk>[0-9]+)/$', views.QuestionsDetail.as_view()),
    url(r'tutorials/$', views.TutorialsList.as_view()),
    url(r'tutorials/(?P<pk>[0-9]+)/$', views.TutorialsDetail.as_view()),
    url(r'formulae/$', views.FormulaeList.as_view()),
    url(r'formulae/(?P<pk>[0-9]+)/$', views.FormulaeDetail.as_view()),
]
