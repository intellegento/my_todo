from django.contrib import admin
from .models import ToDo
from .models import ToMeet


admin.site.register(ToDo)
admin.site.register(ToMeet)
