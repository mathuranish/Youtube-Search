from django.urls import path
from . import views

urlpatterns = [
    path("key_list", views.keyList, name="keylist"),
]
