from django.urls import path
from .views import index

urlpatterns = [

    path("all/",index ,name="index"),      # localhost/status/all to access
]
