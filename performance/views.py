from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from performance.models import Book


class PerformanceView(APIView):
    @staticmethod
    def get(request):
        book = Book.objects.get(id=1)

        # -- Let's check the availability of
        # -- an author from Book model

        # --------------------------
        if book.author_id:
            print("passed with author_id without extra query")
        # --------------------------

        # --------------------------
        if book.author:
            print("passed with author_id with an extra query")
        # --------------------------

        return Response(status=status.HTTP_200_OK)
