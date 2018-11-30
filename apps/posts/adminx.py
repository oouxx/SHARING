from .models import Software
from .models import SoftwareDetail
from .models import Opensource
from .models import OpensourceDetail
from .models import Programming
from .models import ProgrammingDetail
import xadmin


class SoftwareAdmin(object):
    list_display = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    list_filter =  ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no" ]
    search_fields = ["title", "release_person", "contribute_person", "comment_no", "like_no"]


    class SoftwareDetailInline(object):
        model = SoftwareDetail
        exclude = []
        extra = 1
        style = 'tab'

    inlines = [SoftwareDetailInline]

class OpensourceAdmin(object):
    list_display = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    list_filter = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    search_fields = ["title", "release_person", "contribute_person", "comment_no", "like_no"]
    class OpensourceDetailInline(object):
        model = OpensourceDetail
        exclude = []
        extra = 1
        style = 'tab'

    inlines = [OpensourceDetailInline]


class ProgrammingAdmin(object):
    list_display = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    list_filter = ["title", "release_person", "contribute_person", "release_time", "modify_time", "comment_no", "like_no"]
    search_fields = ["title", "release_person", "contribute_person", "comment_no", "like_no"]

    class ProgrammingDetailInline(object):
        model = ProgrammingDetail
        exclude = []
        extra = 1
        style = 'tab'

    inlines = [ProgrammingDetailInline]

xadmin.site.register(Software, SoftwareAdmin)
xadmin.site.register(Opensource, OpensourceAdmin)
xadmin.site.register(Programming, ProgrammingAdmin)

