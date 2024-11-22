from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import viewsets
from .models import User 
from .serializers import UserSerializer
from handlers.response import custom_response
from django.contrib.auth.hashers import make_password
from starlette import status

class UserViewSet(viewsets.ViewSet):
  def list(self, request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, many=True)
    return custom_response("Lista de usuarios",serializer.data,False,status.HTTP_200_OK)
  
  def retrieve(self, request, pk=None):
    try:
      user = User.objects.get(id=pk)
      serializer = UserSerializer(user)
      return custom_response("Usuario encontrado",serializer.data,False,status.HTTP_200_OK)
    except User.DoesNotExist:
      return custom_response("Usuario no encontrado",None,True,status.HTTP_404_NOT_FOUND)
  
  def create(self, request):
    # Crear una copia mutable de los datos del request
    data = request.data.copy()
    # Obtener el password y encriptarlo
    password = data.get('password')
    data['password'] = make_password(password)
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return custom_response("Usuario creado",serializer.data,False,status.HTTP_201_CREATED)
    return custom_response("Error al crear usuario",serializer.errors,True,status.HTTP_400_BAD_REQUEST)
  
  def patch(self, request, pk=None):
    user = User.objects.get(id=pk)
    data = request.data
    user.username = data.get('username')
    user.role = data.get('role')
    user.email = data.get('email')
    user.save()
    serializer = UserSerializer(user)
    return custom_response("Usuario actualizado",serializer.data,False,status.HTTP_200_OK)
  
  def put(self, request, pk=None):
    print("PUT")
    print(pk)
    try:
        # Intentar obtener al usuario con el id 'pk'
        user = User.objects.get(id=pk)
        data = request.data

        # Verificar si el nombre de usuario coincide
        username = data.get('username')
        if user.username == username:
            # Si el nombre de usuario es correcto, actualizar la contraseña
            new_password = data.get('password')
            if new_password:
                user.password = make_password(new_password)
                user.save()
                serializer = UserSerializer(user)
                return custom_response("Contraseña actualizada", serializer.data, False, status=status.HTTP_200_OK)
            else:
                return custom_response("La nueva contraseña no puede estar vacía",[], True, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Si el nombre de usuario no coincide
            return custom_response("Usuario no encontrado",[], True, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        # Si no se encuentra el usuario
        return custom_response("Usuario no encontrado", [], True, status=status.HTTP_404_NOT_FOUND)
    
  def delete(self, request, pk=None):
    try:
      user = User.objects.get(id=pk)
      user.delete()
      return custom_response("Usuario eliminado",None,False,status.HTTP_200_OK)
    except User.DoesNotExist:
      return custom_response("Usuario no encontrado",None,True,status.HTTP_404_NOT_FOUND)

class AutehnticateViewSet(viewsets.ViewSet):
  def create(self, request):
    data = request.data
    username = data.get('username')
    password = data.get('password')
    print(username)
    print(password)
    user = User.aunthenticate(username, password)
    if user:
      serializer = UserSerializer(user)
      return custom_response("Usuario autenticado",serializer.data,False,status.HTTP_200_OK)
    return custom_response("Usuario no encontrado",None,True,status.HTTP_404_NOT_FOUND)