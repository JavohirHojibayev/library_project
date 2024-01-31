from turtle import title
from turtle import Turtle

from rest_framework import serializers
from  .models import  Book
from rest_framework.exceptions import ValidationError
from django.core.exceptions import ValidationError
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id','title','content', 'subtitle', 'author', 'isbn', 'price')


    def validate(self, data):
        title = data.get('title', None),
        author = data.get('author', None)

        #check alphabetical  chars
        if not title.isalpha():
            raise ValidationError({
                "status": False,
                "message": "Title must be alphanumeric"
            })
        return data

        #check database existanse

        if Book.objects.filter(title=title, author= author).exists():
          raise ValidationError({
            "status": False,
            "message": "Kitob sarlavhasi va muallifi bir xil !!!"
        })
        return data


