from django.contrib import admin
from . import models

# Register your models here.


class ThreadMemberInline(admin.TabularInline):
     model = models.ThreadMember

admin.site.register(models.Thread)
