from django.urls import path
from .views import *

urlpatterns = [
    path('tanlanganlar/', TanlanganlarView.as_view()),
    path('buyurtmalar/', BuyurtmalarView.as_view()),
    path('savatlar/', SavatlarView.as_view()),
    path('miqdor_q/<int:pk>/', MiqdorQosh.as_view()),
    path('miqdor_k/<int:pk>/', MiqdorKamaytir.as_view()),
    path('t_ochir/<int:pk>/', TalanganDelete.as_view()),

]
