from django.urls import path
from gift_cards_app import views

app_name = 'gift_cards_app'

urlpatterns = [
    path('', views.order_form, name='order_form')
]
