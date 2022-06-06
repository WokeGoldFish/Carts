import imp
from tkinter.ttk import Style
from rest_framework import serializers
from django.apps import apps
from django.contrib.auth.models import User

Post = apps.get_model('ecom', 'Post')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
        
class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only = True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        extra_kwarfs = {
            'password': {'write_only': True}
        }
        
    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
            
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password' : 'Passwords must Match'})
        user.set_password(password)
        user.save()
        return user