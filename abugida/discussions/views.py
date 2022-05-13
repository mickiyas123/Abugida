from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic, Questions, User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import RoomForm



def discussions(request):
   q = request.GET.get('q') if request.GET.get('q') != None else ''

   rooms = Room.objects.filter(
      Q(topic__name__icontains=q) |
      Q(name__icontains=q) |
      Q(description__icontains=q)
    )

   topics = Topic.objects.all()[0:5]
   room_count = rooms.count()
   room_messages = Questions.objects.filter(
      Q(room__topic__name__icontains=q))[0:3]

   context = {'rooms': rooms, 'topics': topics,
            'room_count': room_count, 'room_messages': room_messages}




   return render(request, 'discussions/discussions.html', context)




@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('discussions')

    context = {'form': form, 'topics': topics}
    return render(request, 'discussions/room_form.html', context) 

