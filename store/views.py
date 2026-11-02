from django.shortcuts import render
from .serilizers import * 
from django.contrib .auth import tokens
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class TaskView(CreateAPIView):
    serializers_class=Taskserilizers
   
class GetView(ListAPIView):
    serializers_class=Taskserilizers
    Authentacation_class = [TokenAuthentication]
    permission_class =[IsAuthenticated]
      
class UpdateView(UpdateAPIView):
    serializers_class=Taskserilizers
    Authentacation_class = [TokenAuthentication]
    permission_class =[IsAuthenticated]
    
    