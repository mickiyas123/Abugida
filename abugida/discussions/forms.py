from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Questions, answers




class RoomForm(ModelForm):

    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'

class AnswerForm(ModelForm):
    class Meta:
        model = answers
        fields = '__all__'

