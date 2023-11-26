from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from asosiy.views import HomeNoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeNoView.as_view()),
    path('user/', include("userapp.urls")),
    path('asosiy/', include("asosiy.urls")),
    path('buyurtma/', include("buyurtma.urls")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
