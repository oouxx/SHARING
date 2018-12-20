from .models import Software
from .models import Opensource
from .models import Programming
from .models import Experience
from .models import Question
import xadmin


class SoftwareAdmin(object):
    list_display = ["title", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    list_filter =  ["title", "contribute_person", "release_time", "modify_time", "comment_no", "like_no" ]
    search_fields = ["title", "contribute_person", "comment_no", "like_no"]


class OpensourceAdmin(object):
    list_display = ["title", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    list_filter = ["title", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    search_fields = ["title", "contribute_person", "comment_no", "like_no"]


class ProgrammingAdmin(object):
    list_display = ["title", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    list_filter = ["title", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    search_fields = ["title", "contribute_person", "comment_no", "like_no"]


class ExperienceAdmin(object):
    list_display = ["title", "release_time", "modify_time", "contribute_person", "description"]
    list_filter = ["contribute_person"]
    search_fields = ["contribute_person", "title"]


class QuestionAdmin(object):
    list_display = ["title", "release_time", "modify_time", "description", "contribute_person"]
    list_filter = ["contribute_person"]
    search_fields = ["contribute_person", "title"]


xadmin.site.register(Software, SoftwareAdmin)
xadmin.site.register(Opensource, OpensourceAdmin)
xadmin.site.register(Programming, ProgrammingAdmin)
xadmin.site.register(Experience, ExperienceAdmin)
xadmin.site.register(Question, QuestionAdmin)
