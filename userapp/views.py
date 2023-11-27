from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, "page-user-login.html")

    def post(self, request):
        user = authenticate(
            username=request.POST.get("login"),
            password=request.POST.get("password")
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/asosiy/home/")


class RegisterView(View):
    def get(self, request):
        return render(request, "page-user-register.html")

class KodTasdiqlash(View):
    def get(self, request):
        return render(request, "tasdiqlash.html")
