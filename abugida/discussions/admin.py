from django.contrib import admin
from .models import Topic, Room, Question, Answer 

# Register your models here.

admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Question)
admin.site.register(Answer)