from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response
from .models import *


class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'
