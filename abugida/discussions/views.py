from django.shortcuts import render, redirect
from .models import Question, Room ,Topic, Answer
from .forms import RoomForm ,QuestionForm ,AnswerForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def discussion(request):
    discussions = Room.objects.all()
    # question = rooms.question_set.all()
    # answer = rooms.answer_set.all()
    context = {'discussions': discussions}
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
    context = {'room': room, 'questions': questions, 'answers': answers}
    return render(request, 'discussions/room.html', context)


@login_required(login_url='login')
def createRoom(request):
    profile = request.user.profile
    """ A method for creating new room """
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)

        if form.is_valid():
            room = form.save(commit=False)
            room.host = profile
            room.save()
            return redirect('discussion')
    context = {'form': form}
    return render(request, 'discussions/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request, pk):
    """ A method for updating a room """
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)

        if form.is_valid():
            form.save()
            return redirect('discussion')
    context = {'form': form}
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
    return render(request, 'discussions/question_form.html', context)


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
def createAnswer(request):
    """ a method for creating an answer """
    form = AnswerForm()

    if request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('discussion')
    context = {'form': form}
    return render(request, 'discussions/answer_form.html', context)



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
