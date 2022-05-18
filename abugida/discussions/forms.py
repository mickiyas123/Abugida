from django.forms import ModelForm
from .models import Room ,Question, Answer

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['body','body_image']

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['body']