from unicodedata import name
from django.shortcuts import render, redirect
from .models import Question, Room ,Topic, Answer
from .forms import RoomForm ,QuestionForm ,AnswerForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'discussions/index.html')

def about(request):
    return render(request, 'discussions/about.html')

def course(request):
    return render(request, 'discussions/course.html')

def discussion(request):
    discussions = Room.objects.all()
    # question = rooms.question_set.all()
    # answer = rooms.answer_set.all()
    answer_form = AnswerForm()
    context = {'discussions': discussions, 'answer_form': answer_form}
    
    return render(request, 'discussions/discussions.html', context)

# def topic(request):
#     topics = Topic.objects.all()
#     context = {'topics': topics}
#     return render(request, 'discussions/topic.html', context)

def rooms(request):
    """ A method that shows list of rooms """
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'discussions/rooms.html', context)


def room(request, pk):
    """ A method that shows a specific room"""
    room = Room.objects.get(id=pk)
    questions = room.question_set.all()
    answers = room.answer_set.all()
    question_form = QuestionForm()
    answer_form = AnswerForm()
    context = {'room': room, 'questions': questions, 'answers': answers, 'question_form': question_form, 'answer_form': answer_form}
    return render(request, 'discussions/room.html', context)


@login_required(login_url='login')
def createRoom(request):
    """ A method for creating new room """
    profile = request.user.profile
    topics = Topic.objects.all()
    form = RoomForm()

    if request.method == 'POST':
        topic_name = request.POST.get("topic")
        topic_names = []
        for topic in topics:
            topic_names.append(topic.name)
        
        if topic_name not in topic_names:
            topic = Topic.objects.create(
                    name=topic_name, creator=profile)
        else:
            topic = Topic.objects.get(name=topic_name)

        new_room = Room.objects.create(
            host=profile,
            topic=topic,
            name = request.POST.get("name"),
            description = request.POST.get("description")
        )
        return redirect('rooms')
    context = {'form': form, 'topics': topics}
    return render(request, 'discussions/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request, pk):
    """ A method for updating a room """
    profile = request.user.profile
    room = Room.objects.get(id=pk)
    topic = room.topic
    topics = Topic.objects.all()
    form = RoomForm(instance=room)

    if request.method == 'POST':
        topic_name = request.POST.get("topic")
        topic.name = topic_name
        topic.save()

        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get("description")
        room.save()
        
        return redirect('discussion')
    context = {'form': form, 'room':room, 'topics': topics}
    return render(request, 'discussions/room_form.html', context)




@login_required(login_url='login')
def createQuestion(request, pk):
    """ A method for creating question """
    querier = request.user.profile
    room = Room.objects.get(id=pk)
    body = request.POST.get("body")
    topic = room.topic

    if request.method == 'POST':
        Question.objects.create(
            querier = querier,
            room = room,
            body = body,
            topic = topic
        )
        return redirect('room', pk=room.id)



@login_required(login_url='login')
def updateQuestion(request, pk):
    """ A method for updating specific question """
    question = Question.objects.get(id=pk)
    form = QuestionForm(instance=question)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)

        if form.is_valid():
            form.save()
            return redirect('discussion')
    context = {'form': form}
    return render(request, 'discussions/question_form.html', context)


@login_required(login_url='login')
def createAnswer(request, pk):
    """ a method for creating an answer """
    responder = request.user.profile
    question = Question.objects.get(id=pk)
    body = request.POST.get("body")
    room = question.room
    topic = room.topic

    if request.method == 'POST':
        Answer.objects.create(
            responder= responder,
            question = question,
            room = room,
            body = body,
            topic = topic
        )
        return redirect('discussion')



@login_required(login_url='login')
def updateAnswer(request, pk):
    """ a method for updating specific question """
    answer = Answer.objects.get(id=pk)
    form = AnswerForm(instance=answer)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)

        if form.is_valid():
            form.save()
            return redirect('discussion')
    context = {'form': form}
    return render(request, 'discussions/answer_form.html', context)


@login_required(login_url='login')
def deleteRoom(request, pk):
    """ A method for deleteing a room """
    room = Room.objects.get(id=pk)
    # question = Question.objects.get(id=pk)
    # answer = Answer.objects.get(id=pk)

    if request.method == 'POST':
        room.delete()
        return redirect('discussion')
    return render(request, 'discussions/delete.html', {'obj': room})


@login_required(login_url='login')
def deleteQuestion(request, pk):
    """ A method for deleting a question """
    question = Question.objects.get(id=pk)
    # question = Question.objects.get(id=pk)
    # answer = Answer.objects.get(id=pk)

    if request.method == 'POST':
        question.delete()
        return redirect('discussion')
    return render(request, 'discussions/delete.html', {'obj': question})


@login_required(login_url='login')
def deleteAnswer(request, pk):
    """ A method for deleting an answer """
    answer = Answer.objects.get(id=pk)
    # question = Question.objects.get(id=pk)
    # answer = Answer.objects.get(id=pk)

    if request.method == 'POST':
        answer.delete()
        return redirect('discussion')
    return render(request, 'discussions/delete.html', {'obj': answer})
