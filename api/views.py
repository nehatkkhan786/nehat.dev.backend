from django.shortcuts import render
from .serializers import ContactEmailSerializer
from nehat.models import ContactEmail
from rest_framework.views import APIView
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
         