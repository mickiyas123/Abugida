from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def loginUser(request):
    """ A function for logging in user """
    page = 'login'

    context = {'page': page}
    if request.user.is_authenticated:
        return redirect('discussion')

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
    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    """ A function to logout user """
    logout(request)
    return redirect('discussion')

def registerUser(request):
    """ A function to register new user """
    page = 'register'
    form  = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=True)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            return redirect('edit-account')

    context = {'page': page, 'form': form}

    return render(request, 'users/login_register.html', context)


def profile(request, pk):
    """ A function for retreving profile """
    profile = Profile.objects.get(id=pk)
    context ={'profile': profile}
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    """ A function for editing profile """
    profile = request.user.profile

    rooms = profile.room_set.all()
    context = {'profile': profile, 'rooms': rooms}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('account')
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)
