from django.forms import ModelForm
from .models import Room ,Question, Answer

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'