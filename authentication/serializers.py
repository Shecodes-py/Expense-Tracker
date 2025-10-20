from rest_framework import serializers
from django.contrib.auth.models import User
# from django.contrib.auth.models import User
#from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        #user.save()
        return user
