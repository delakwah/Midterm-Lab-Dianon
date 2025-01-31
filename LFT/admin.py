from django.contrib import admin
from .models import LostItem, Report, Claim, Message
# Register your models here.

admin.site.register(LostItem)
admin.site.register(Report)
admin.site.register(Claim)
admin.site.register(Message)
