from .models import Software
from .models import Opensource
from .models import Hacker
from .models import Programming
import xadmin


class SoftwareAdmin(object):
    list_display = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no", "type", "description"]
    list_filter =  ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no", "type"]
    search_fields = ["title", "release_person", "contribute_person", "comment_no", "like_no", "type"]


class OpensourceAdmin(object):
    list_display = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no", "project_addr", "description"]
    list_filter = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    search_fields = ["title", "release_person", "contribute_person", "comment_no", "like_no"]


class HackerAdmin(object):
    pass

class ProgrammingAdmin(object):
    list_display = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no", "type", "description"]
    list_filter = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no", "type"]
    search_fields = ["title", "release_person", "contribute_person", "comment_no", "like_no", "type"]


xadmin.site.register(Software, SoftwareAdmin)
xadmin.site.register(Opensource, OpensourceAdmin)
xadmin.site.register(Hacker, HackerAdmin)
xadmin.site.register(Programming, ProgrammingAdmin)

