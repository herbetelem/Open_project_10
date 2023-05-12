from django.contrib import admin
from .models import Comment, Issue, Project, Contributor

# Register your models here.
admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Comment)
