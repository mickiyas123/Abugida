from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic, Questions, User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import RoomForm, QuestionForm



def discussions(request):
   q = request.GET.get('q') if request.GET.get('q') != None else ''

   rooms = Room.objects.filter(
      Q(topic__name__icontains=q) |
      Q(name__icontains=q) |
      Q(description__icontains=q)
    )

   topics = Topic.objects.all()[0:5]
   room_count = rooms.count()
   room_discription = Room.description
   room_messages = Questions.objects.filter(
      Q(room__topic__name__icontains=q))[0:3]

   context = {'rooms': rooms, 'topics': topics,
            'room_count': room_count, 'room_messages': room_messages, 'room_discription': room_discription}




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

@login_required(login_url='login')
def createQuestion(request):
    """ A method for creating question """
    form = QuestionForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('discussion')
    context = {'form': form}
    return render(request, 'discussions/questions_form.html', context)