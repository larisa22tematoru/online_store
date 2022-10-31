from django import views
from . import views
from django.urls import path

app_name = 'footer'

urlpatterns = [
    path('politica-de-retur/', views.politica_de_retur, name='politica_de_retur'),
    path('touch-of-gold-club/', views.touch_of_gold_club, name='touch_of_gold_club'),
    path('responsabilitate/', views.responsabilitate, name='responsabilitate'),
    path('setari-cookieuri/', views.setari_cookieuri, name='setari_cookieuri'),

]