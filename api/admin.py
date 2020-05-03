from django.contrib import admin

# Register your models here.
from api.models import User, Kanban

admin.site.register(User)
admin.site.register(Kanban)