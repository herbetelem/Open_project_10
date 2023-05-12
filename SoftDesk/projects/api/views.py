# import python

# import django
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# import tier
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated

# import perso
from projects.models import Project, Contributor, Issue, Comment
from .serializers import ProjectSerializer, ContributorSerializer,CommentSerializer, IssueSerializer
from .persmissions import IsOnProjectPermission



class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # potentiel moyen pour requerir l'auth pour avoir acces au data
    permission_classes = [IsAuthenticated, IsOnProjectPermission]

    def update(self, request, *args, **kwargs):
        contributors = Contributor.objects.filter(
            user_id=request.user,
            project_id__id=self.get_object().project_id.id,
            permission='editor')
        if contributors:
            return super().update(request, *args, **kwargs)
        return None

    def destroy(self, request, *args, **kwargs):
        user = request.user
        project_tmp = self.get_object()
        if project_tmp.author_user_id == user:
            return super().destroy(request, *args, **kwargs)
        return None
        
    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)

class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsOnProjectPermission]

    def create(self, request, *args, **kwargs):
        contributors = Contributor.objects.filter(
            user_id=request.user,
            project_id__id=self.get_object().project_id.id,
            permission='editor')
        if contributors:
            return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        contributors = Contributor.objects.filter(
            user_id=request.user,
            project_id__id=self.get_object().project_id.id,
            permission='editor')
        if contributors:
            return super().update(request, *args, **kwargs)
        return None

    def destroy(self, request, *args, **kwargs):
        user = request.user
        project_tmp = self.get_object()
        if project_tmp.author_user_id == user:
            return super().destroy(request, *args, **kwargs)
        return None

    def get_queryset(self):
        return Contributor.objects.filter(project_id=self.kwargs['projects_pk'])


class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsOnProjectPermission]

    def create(self, request, *args, **kwargs):
        contributors = Contributor.objects.filter(
            user_id=request.user,
            project_id__id=self.get_object().project_id.id,
            permission='editor')
        if contributors:
            return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        contributors = Contributor.objects.filter(
            user_id=request.user,
            project_id__id=self.get_object().project_id.id,
            permission='editor')
        if contributors:
            return super().update(request, *args, **kwargs)
        return None
    
    def destroy(self, request, *args, **kwargs):
        user = request.user
        project_tmp = self.get_object()
        if project_tmp.author_user_id == user:
            return super().destroy(request, *args, **kwargs)
        return None

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs['projects_pk'])
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOnProjectPermission]

    def create(self, request, *args, **kwargs):
        contributors = Contributor.objects.filter(
            user_id=request.user,
            project_id__id=self.get_object().project_id.id,
            permission='editor')
        if contributors:
            return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        contributors = Contributor.objects.filter(
            user_id=request.user,
            project_id__id=self.get_object().project_id.id,
            permission='editor')
        if contributors:
            return super().update(request, *args, **kwargs)
        return None

    def destroy(self, request, *args, **kwargs):
        user = request.user
        project_tmp = self.get_object()
        if project_tmp.author_user_id == user:
            return super().destroy(request, *args, **kwargs)
        return None

    def get_queryset(self):
        print(self.kwargs)
        return Comment.objects.filter(issue_id=self.kwargs['issues_pk'])
    
    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)