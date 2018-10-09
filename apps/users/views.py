
# Create your views here.

from django.views.generic import View
from django.shortcuts import render

class Login(View):

    def get(self, request):
        return render(request, "login.html")
    def post(self, request):
        try:
            from django.contrib.auth import authenticate, login
            self.user_name = request.POST.get("username", "")
            self.pass_word = request.POST.get("password", "")
            user = authenticate(username=self.user_name, password= self.pass_word)
            if user is not None:
                login(request, user)
                return render(request, "login_success.html", {})
        except:
            print("login failed")
            return render(request, "index.html", {})
