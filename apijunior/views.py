from django.shortcuts import redirect
from rest_framework import generics 
from rest_framework.response import Response
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User,Child,Image,Game
from .serializers import ChildLoginSerializer, UserSerializer, UserLoginSerializer, UserLogoutSerializer,ChildSerializer,ImageSerializer,GameSerializer


class Record(generics.ListCreateAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Login(generics.GenericAPIView):
    # get method handler

    queryset = User.objects.all(), Child.objects.all()
    serializer_class = UserLoginSerializer
    # post method
    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        cserializer_class = ChildLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True) or cserializer_class.is_valid(raise_exception=True):
            if serializer_class.is_valid(raise_exception=True):
                return Response(serializer_class.data, status=HTTP_200_OK)
            if cserializer_class.is_valid(raise_exception=True):
                return Response(serializer_class.data, status=HTTP_200_OK)
        else:
            return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)

class cLogin(generics.GenericAPIView):
    # get method handler

    queryset = Child.objects.all()
    serializer_class = ChildLoginSerializer
    # post method
    def post(self, request, *args, **kwargs):
        serializer_class = ChildLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)
# logout 
class Logout(generics.GenericAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)

        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)

class Addchild(generics.ListCreateAPIView):
    # get method handler
    queryset = Child.objects.all()
    serializer_class = ChildSerializer  


class Addimage(generics.ListCreateAPIView):
    
    queryset = Image.objects.all()
    serializer_class = ImageSerializer 




class Addgame(generics.ListCreateAPIView):
    
    queryset = Game.objects.all()
    serializer_class = GameSerializer