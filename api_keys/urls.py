from django.urls import path
from . import views

urlpatterns = [
    path("keylist/", views.keyList, name="keylist"),
    path("keydelete/<int:key_id>", views.keyDelete, name="keydelete"),
]
