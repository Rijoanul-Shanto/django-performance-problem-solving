from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from performance.models import Book


class PerformanceView(APIView):
    @staticmethod
    def get(request):
        query = Book.objects.all()
        print(query)
        return Response(status=status.HTTP_200_OK)
