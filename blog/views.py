from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog,Category
from .serialization import BlogSerializer, CategorySerializer
# Create your views here.

class BlogList (APIView):
    def get(self, request):
        blogs=Blog.objects.all()
        serializer=BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogDetailView(APIView):
    def get(self, request, pk):
        try:
            blog=Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({"error":"Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=BlogSerializer(blog)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            blog=Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response({"error":"blog not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer=BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        blog=get_object_or_404(Blog, pk=pk)
        blog.delete()
        return Response({"message":"blog deleted"},status=status.HTTP_204_NO_CONTENT)     