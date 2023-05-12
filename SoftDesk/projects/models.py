from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    TYPE_CHOICE = (
        ('dev', 'dev'),
        ('model', 'model'),
        ('word', 'word'),
    )
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    typ = models.CharField(choices=TYPE_CHOICE, default='dev', max_length=128)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    PERMISSION_CHOICE = (
        ('editor', 'editor'),
        ('reader', 'reader'),
    )
    ROLE_CHOICE = (
        ('admin', 'admin'),
        ('editor', 'editor'),
        ('reader', 'reader'),
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey("Project", on_delete=models.CASCADE)
    role = models.CharField(choices=PERMISSION_CHOICE, default='reader', max_length=128)
    permission = models.CharField(choices=PERMISSION_CHOICE, default='reader', max_length=10)

    def __str__(self):
        name = self.user_id.username + ": " + self.project_id.title
        return name

class Issue(models.Model):
    TAG_CHOICE = (
        ('Not view', 'Not view'),
        ('View', 'View'),
        ('Fix', 'Fix'),
    )
    PRIORITY_CHOICE = (
        ('urgent', 'urgent'),
        ('primary', 'primary'),
        ('secondary', 'secondary'),
    )
    STATUS_CHOICE = (
        ('To do', 'To do'),
        ('doing', 'doing'),
        ('done', 'done'),
    )

    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=128)
    tag = models.CharField(choices=TAG_CHOICE, default='Not view', max_length=128)
    priority = models.CharField(choices=PRIORITY_CHOICE, default='secondary', max_length=128)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_to_assign")
    status = models.CharField(choices=STATUS_CHOICE, default='To do', max_length=128)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    description = models.CharField(max_length=128)
    author_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_id = models.ForeignKey("Issue", on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:20]