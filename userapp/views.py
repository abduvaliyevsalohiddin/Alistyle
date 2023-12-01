from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.conf import settings
from django.views import View
from .models import *
import random
from eskiz.client import SMSClient


class LoginView(View):
    def get(self, request):
        return render(request, "page-user-login.html")

    def post(self, request):
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is None:
            return redirect('/user/login/')
        login(request, user)
        return redirect('/asosiy/home/')


class RegisterView(View):
    def get(self, request):
        return render(request, "page-user-register.html")

    def post(self, request):
        profil = Profil.objects.create_user(
            username=request.POST.get("t"),
            password=request.POST.get("p1"),
            tel=request.POST.get("t"),
            first_name=request.POST.get("f"),
            last_name=request.POST.get("l"),
            davlat=request.POST.get("d"),
            shahar=request.POST.get("sh"),
            jins=request.POST.get("gender"),
            tasdiqlash_kodi=random.randrange(10000, 100000)

        )
        mijoz = SMSClient(
            api_url="https://notify.eskiz.uz/api/",
            email=settings.ESKIZ_GMAIL,
            password=settings.ESKIZ_PAROL,
        )
        mijoz._send_sms(
            phone_number=profil.tel,
            message=f"Alistyle loyihasidagi tasdiqlash kodingiz:"
                    f"          {profil.tasdiqlash_kodi}",
        )
        login(request, profil)
        return redirect("/user/tasdiqlash/")


class KodTasdiqlash(View):
    def get(self, request):
        return render(request, "kod-tasdiqlash.html")

    def post(self, request):
        profil = Profil.objects.get(id=request.user.id)
        if profil.tasdiqlash_kodi == request.POST.get("k"):
            profil.tasdiqlangan = True
            profil.save()
            return redirect("/user/login/")
        return redirect("/user/tasdiqlash/")
