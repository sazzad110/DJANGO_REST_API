from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Status
from .serializers import StatusSerializer

# Create your views here.

class StatusViewer(APIView):
    def get(self,request):
        all_status = Status.objects.all()
        serializer = StatusSerializer(all_status,many=True)
        return Response(serializer.data)