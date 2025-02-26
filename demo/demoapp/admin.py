from django.contrib import admin
from demoapp.models import Category, Course, Lesson, Tag
from django.utils.safestring import mark_safe





class MyLessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'active', 'course']
    search_fields = ['subject']
    list_filter = ['id', 'created_date']
    readonly_fields = ['img_view']

    def img_view(self, lesson):
        return mark_safe(f"<img src='/static/{lesson.image.name}' width='200px'>")

    class Media:
        css = {
            'all': ('/static/css/style.css', )
        }


class MyCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'active', 'description']
    search_fields = ['subject']
    list_filter = ['id', 'created_date']
    readonly_fields = ['img_view']

    def img_view(self, course):
        return mark_safe(f"<img src='/static/{course.image.name}' width='200px'>")

admin.site.register(Category)
admin.site.register(Course, MyCourseAdmin)
admin.site.register(Lesson, MyLessonAdmin)
admin.site.register(Tag)
