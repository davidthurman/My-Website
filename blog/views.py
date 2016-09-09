from django.shortcuts import render

from .models import Topic, Project
# Create your views here.
def index(request):
	"""The home page for my website"""
	return render(request, 'blog/index.html')

def topics(request):
	"""Show all topics"""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'blog/topics.html', context)

def topic(request, topic_id):
	"""Show a single topic and all its entries"""
	topic = Topic.objects.get(id = topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'blog/topic.html', context)

def about(request):
	"""The about page for my website"""
	return render(request, 'blog/about.html')

def projects(request):
	"""The Projects page for my website"""
	projects = Project.objects.order_by('date_added')
	context = {'projects': projects}
	return render(request, 'blog/projects.html', context)

def project(request, project_id):
	"""A more in depth view of the project with pictures"""
	project = Project.objects.get(id = project_id)
	pictures = project.picture_set.order_by('id')
	context = {'pictures': pictures, 'project': project}
	return render(request, 'blog/project.html', context)