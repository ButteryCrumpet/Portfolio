from django.contrib import admin

from . models import Project, AdditionalImage, Language
# Register your models here.

admin.site.register(Project)
admin.site.register(AdditionalImage)
admin.site.register(Language)
