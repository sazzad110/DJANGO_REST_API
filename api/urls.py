from django.urls import path

from status.views import StatusViewer

urlpatterns = [

    path("status/<int:id>/",StatusViewer.as_view() ,name="status_view"), 
]
