from .models import Software
from .models import Opensource
from .models import Programming
from .models import Experience
from .models import Question
from django.contrib import admin


class SoftwareAdmin(admin.ModelAdmin):
    list_display = ["title", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    list_filter =  ["title", "contribute_person", "release_time", "modify_time", "comment_no", "like_no" ]
    search_fields = ["title", "contribute_person", "comment_no", "like_no"]


class OpensourceAdmin(admin.ModelAdmin):
    list_display = ["title", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    list_filter = ["title", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    search_fields = ["title", "contribute_person", "comment_no", "like_no"]


class ProgrammingAdmin(admin.ModelAdmin):
    list_display = ["title", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    list_filter = ["title", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    search_fields = ["title", "contribute_person", "comment_no", "like_no"]


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["title", "release_time", "modify_time", "contribute_person", "description"]
    list_filter = ["contribute_person"]
    search_fields = ["contribute_person", "title"]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["title", "release_time", "modify_time", "description", "contribute_person"]
    list_filter = ["contribute_person"]
    search_fields = ["contribute_person", "title"]


admin.site.register(Software, SoftwareAdmin)
admin.site.register(Opensource, OpensourceAdmin)
admin.site.register(Programming, ProgrammingAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Question, QuestionAdmin)

