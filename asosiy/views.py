from django.shortcuts import render
from django.views import View
from .models import *
from django.db.models import Avg


class HomeNoView(View):
    def get(self, request):
        content = {
            "bolimlar": Bolim.objects.all()[:8]
        }
        return render(request, "page-index-2.html")


class HomeView(View):
    def get(self, request):
        content = {
            "bolimlar": Bolim.objects.all()[:8]
        }
        return render(request, "page-index.html", content)


class BolimlarView(View):
    def get(self, request):
        content = {
            "bolimlar": Bolim.objects.all()
        }
        return render(request, "page-category.html", content)


class MahsulotlarView(View):
    def get(self, request, pk):
        content = {
            "mahsulotlar": Mahsulot.objects.filter(bolim__id=pk)
        }
        return render(request, "page-listing-grid.html", content)


class MahsulotView(View):
    def get(self, request, pk):
        izohlar = Izoh.objects.filter(mahsulot__id=pk)
        ortachasi = izohlar.aggregate(Avg("baho")).get("baho__avg")
        if ortachasi:
            ortachasi *= 20
        else:
            ortachasi = 0
        content = {
            "mahsulot": Mahsulot.objects.get(id=pk),
            "ortachasi": ortachasi
        }
        return render(request, "page-detail-product.html", content)
