from django.shortcuts import render, HttpResponse

from .models import *

from rest_framework.viewsets import ModelViewSet
from .serializers import BookInfoSerializer
from .models import BookInfo


def show_book_info(request):
    query_set = BookInfo.objects.all()
    book_info = ''

    for query in query_set:
        book_info += '{} - {} - {} <br />'.format(query.author, query.title, query.pub_date)

    return HttpResponse(book_info)


class BookInfoViewSet(ModelViewSet):
   queryset = BookInfo.objects.all()
   serializer_class = BookInfoSerializer
