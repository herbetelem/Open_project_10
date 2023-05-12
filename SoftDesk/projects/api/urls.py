

from importlib.resources import path

from rest_framework_nested import routers
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register("projects", views.ProjectViewSet, basename="projects")
projects_router = routers.NestedDefaultRouter(router, r'projects', lookup='projects')

projects_router.register("contributors", views.ContributorViewSet, basename="contributors")

projects_router.register(r'issues', views.IssueViewSet, basename='issues')
router.register("issues", views.IssueViewSet, basename="issues")

projects_router.register(r'contributors', views.ContributorViewSet, basename='contributors')
router.register("contributors", views.ContributorViewSet, basename="contributors")


issues_router = routers.NestedDefaultRouter(projects_router, r'issues', lookup='issues')
issues_router.register(r'comments', views.CommentViewSet, basename='issues')

urlpatterns = [
    path("", include(router.urls)),
    path("", include(projects_router.urls)),
    path("", include(issues_router.urls)),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

