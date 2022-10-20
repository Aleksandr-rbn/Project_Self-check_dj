from django.contrib import admin
from .models import Option, Riddle, Mark, Message

admin.site.register(Riddle)
admin.site.register(Option)
admin.site.register(Message)
admin.site.register(Mark)