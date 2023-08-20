from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner
from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# <HINT> Register QuestionInline and ChoiceInline classes here
class ChoiceInline(admin.TabularInline):   # or admin.StackedInline
    model = Choice
    extra = 3   # This will show 3 empty Choice fields by default

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['text', 'course', 'grade_point']}),
    ]
    inlines = [ChoiceInline]

# Now, unregister and re-register the Question model to attach the new admin configuration
if admin.site.is_registered(Question):
    admin.site.unregister(Question)

admin.site.register(Question, QuestionAdmin)


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
