from django.urls import path
from .views import board_list, board_detail

app_name = "app"

urlpatterns = [
    path('boards/', board_list, name='board_list'),
    path('boards/<int:pk>/', board_detail, name='board_detail'),
]