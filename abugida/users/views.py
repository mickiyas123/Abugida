from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.


def loginUser(request):
    """ A function for logging in user """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            print("User doesn't exists")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('discussion')
        else:
            print("username or password is incorrect")
    return render(request, 'users/login_register.html')


def logoutUser(request):
    """ A function to logout user """
    logout(request)
    return redirect('discussion')

def profile(request, pk):
    """ A function for retreving profile """
    profile = Profile.objects.get(id=pk)
    context ={'profile': profile}
    return render(request, 'users/profile.html', context)