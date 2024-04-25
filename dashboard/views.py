from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .mysql import MysqlProcessor
from .models import Camera, Iot, Drone
import json

@api_view(['GET'])
def get_all_data(request):
    db = MysqlProcessor()
    devices = db.get_all_devices()
    return Response(devices, status=status.HTTP_200_OK)

