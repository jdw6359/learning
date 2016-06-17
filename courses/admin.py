from django.contrib import admin

# Register your models here.
from .models import Course
from .models import Step

# Define the step inline
class StepInline(admin.StackedInline):
	model = Step

# Configure the Course admin to use the step inline
class CourseAdmin(admin.ModelAdmin):
	inlines = [StepInline,]

admin.site.register(Course, CourseAdmin)
admin.site.register(Step)