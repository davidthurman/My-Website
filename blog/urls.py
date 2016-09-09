"""Defines URL patterns for my website"""

from django.conf.urls import url

from . import views

urlpatterns = [
	#Home page
	url(r'^$', views.index, name='index'),

	#Show all Topics
	url(r'^topics/$', views.topics, name = 'topics'),

	#Detail page for a single topic
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),

	url(r'^about/', views.about, name = 'about'),

	url(r'^projects/$', views.projects, name = 'projects'),

	url(r'^projects/(?P<project_id>\d+)/$', views.project, name = 'project'),
	]