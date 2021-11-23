from django.contrib import admin

# Register your models here.
from .models import Assignment,Location,Applicant

class AssignmentAdmin(admin.ModelAdmin):
	list_display = ('title' , 'slug')
	list_filter =  ('location',)
	prepopulated_fields = {'slug':('title',)}

admin.site.register(Assignment,AssignmentAdmin)
admin.site.register(Location)
admin.site.register(Applicant)