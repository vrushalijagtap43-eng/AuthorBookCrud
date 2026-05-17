from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import  status
from sharpapp.models import Author
from .serializer import AuthorSeriliazers
from rest_framework.response import Response

# Create your views here.


class AuthorCrud(APIView):

    def get(self, request):
        author = Author.objects.all()
        serilizer = AuthorSeriliazers(author,many=True)
        return Response(serilizer.data)

    def post(self, request):
        seriliazer = AuthorSeriliazers(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(seriliazer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        try:
            author=Author.objects.get(id=id)
        except Author.DoesNotExist:
            return Response("not exist",status=status.HTTP_404_NOT_FOUND)
        serializer=AuthorSeriliazers(author, data=request.data,  partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)





