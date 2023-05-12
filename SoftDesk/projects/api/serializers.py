from rest_framework import serializers
from projects.models import Project, Contributor,Comment, Issue

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id", "title", "description", "typ")

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ("id", "project_id", "role", "permission", "user_id")

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ("title", "desc", "tag", "priority", "project_id", "assignee_user_id", "status", "created_time")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("description", "issue_id", "created_time")
