from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .mysql import MysqlProcessor

@api_view(['GET'])
def get_all_notifications(request):
    db = MysqlProcessor()
    notifications = db.process_notifications()
    return Response(notifications, status=status.HTTP_200_OK)
