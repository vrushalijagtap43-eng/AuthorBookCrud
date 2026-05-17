from rest_framework import serializers
from .models import Author, Book


class AuthorSeriliazers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"