from django.shortcuts import render
from .serializers import ContactEmailSerializer, BlogSerializer

from nehat.models import ContactEmail
from blog.models import Blog
from rest_framework.pagination import PageNumberPagination


from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class ConactEmailView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:

            ContactEmail.objects.create(
                name=data['name'],
                email=data['email'], 
                message = data['message'],
            )
        except:
            raise ValidationError('Something went Wrong!')
        return Response({'message':'Message Successfully Created'}, status = status.HTTP_200_OK)
    
class GetAllBlogView(APIView):
    def get (self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100


class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = LargeResultsSetPagination

class BlogDetailView(APIView):
    def get(self, request, pk, *arga, **kwargs):
        try:
            blog = Blog.objects.get(id=pk)
            if blog:
                serializer = BlogSerializer(blog, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message':'Blog Not Found'}, status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'something went wrong'}, status = status.HTTP_404_NOT_FOUND)


   