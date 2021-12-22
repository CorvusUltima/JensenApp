from django.contrib import admin

# Register your models here.
from .models import Assignment,Location,Applicant,Tag


class AssignmentAdmin(admin.ModelAdmin):
	list_display = ('title', )
	list_filter =  ('location',)
	

admin.site.register(Assignment,AssignmentAdmin)
admin.site.register(Location)
admin.site.register(Applicant)
admin.site.register(Tag)