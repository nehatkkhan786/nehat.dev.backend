from rest_framework import serializers
from nehat.models import * 



class ContactEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactEmail
        fields = '__all__'