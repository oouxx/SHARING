from .models import VerifyCode
import xadmin


class VerifyCodeAdmin(object):
    list_display = ["code", "mobile", "add_time"]


xadmin.site.register(VerifyCode, VerifyCodeAdmin)