from django.urls import path
from . import views

urlpatterns = [
    path("<str:msg>", views.index, name="chat"),
]