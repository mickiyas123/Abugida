from django.shortcuts import render
from .models import Profile

# Create your views here.

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context ={'profile': profile}
    return render(request, 'users/profile.html', context)