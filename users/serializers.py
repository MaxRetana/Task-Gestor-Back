from rest_framework import serializers
from .models import User
from django.db.models import Q

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def validate(self, data):
      username = data.get('username')
      email = data.get('email')
      print(f"Validando usuario: {username}, email: {email}")  # Agregar impresión
      if User.objects.filter(Q(username=username) | Q(email=email)).exists():
        print("Ya existe un usuario con ese nombre y correo.")
        raise serializers.ValidationError("Ya existe un usuario con ese nombre y correo.")
      return data
