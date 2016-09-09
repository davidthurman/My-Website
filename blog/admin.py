from django.contrib import admin

from blog.models import Topic, Entry, Project, Picture

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Project)
admin.site.register(Picture)