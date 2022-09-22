from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import UserTheme


# Create your views here.
def home_page(request):
    context = {}
    if request.user.is_authenticated:
        context['theme'] = get_object_or_404(UserTheme, user=request.user)
        return render(request, 'global/home.html', context)
    return render(request, 'global/home.html', context)