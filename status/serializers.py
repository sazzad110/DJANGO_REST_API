from rest_framework import serializers
from status.models import Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id','text','created_at','user']      # id is default field in each model but hidden