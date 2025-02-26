from django.contrib import admin
from demoapp.models import Category, Course, Lesson, Tag

class MyLessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'active', 'course']
    search_fields = ['subject']
    list_filter = ['id', 'created_date']

    class Media:
        css = {
            'all': ('/static/css/style.css', )
        }


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, MyLessonAdmin)
admin.site.register(Tag)
