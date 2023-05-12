from rest_framework import permissions
from ..models import Contributor

class IsOnProjectPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if view.basename == 'project' and view.detail is True:
            project_id = request.parser_context["kwargs"]["pk"]
            users = Contributor.objects.filter(user_id=request.user,project_id__id=project_id)
            if users:
                return True
            return False
        return True