from django.contrib import admin

# Register your models here.
from api.models import User, Board, List, Card

class apiAdmin(admin.ModelAdmin):
    class Meta:
        model = User

admin.site.register([User, Board, List, Card])