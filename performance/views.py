from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from performance.models import Book


class PerformanceView(APIView):
    @staticmethod
    def get(request):
        # book = Book.objects.filter(id=1)

        # -- Let's check the availability of
        # -- an author from Book model

        # --------------------------
        # if book.author_id:
        #     print("passed with author_id without extra query")
        # --------------------------

        # --------------------------
        # if book.author:
        #     print("passed with author_id with an extra query")
        # --------------------------

        # --------------------------
        # book = Book.objects.all().values('title')
        # print('retrieved only book title as Dictionary: ', book)
        # --------------------------

        # --------------------------
        # book = Book.objects.all().values_list('title')
        # print('retrieved only book title as Tuple: ', book)
        # --------------------------

        # --------------------------
        for book in Book.objects.all():
            print('retrieved all book on memory and iterated: ', book)
        # --------------------------

        # --------------------------
        for book in Book.objects.all().iterator():
            print('retrieved book on open sql connection and iterated through database row: ', book)
        # --------------------------

        return Response(status=status.HTTP_200_OK)
