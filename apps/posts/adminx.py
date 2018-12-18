from .models import Software
from .models import Opensource
from .models import Programming
from .models import Experience
from .models import Question
import xadmin


class SoftwareAdmin(object):
    list_display = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    list_filter =  ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no" ]
    search_fields = ["title", "release_person", "contribute_person", "comment_no", "like_no"]


class OpensourceAdmin(object):
    list_display = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    list_filter = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    search_fields = ["title", "release_person", "contribute_person", "comment_no", "like_no"]


class ProgrammingAdmin(object):
    list_display = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    list_filter = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    search_fields = ["title", "release_person", "contribute_person", "comment_no", "like_no"]


class ExperienceAdmin(object):
    list_display = ["user", "title", "release_time", "modify_time", "description"]
    list_filter = ["user"]
    search_fields = ["user", "title"]


class QuestionAdmin(object):
    list_display = ["user","title", "release_time", "modify_time", "description"]
    list_filter = ["user"]
    search_fields = ["user", "title"]


xadmin.site.register(Software, SoftwareAdmin)
xadmin.site.register(Opensource, OpensourceAdmin)
xadmin.site.register(Programming, ProgrammingAdmin)
xadmin.site.register(Experience, ExperienceAdmin)
xadmin.site.register(Question, QuestionAdmin)
