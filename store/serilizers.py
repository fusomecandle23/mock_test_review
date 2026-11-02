from rest_framework import serializers
from .models import Task


class Taskserilizers(serializers.ModelSerializer):
    class meta:
        model = Task
        field ="__all__"
        read_only_field = ['created_at']
        
             

   