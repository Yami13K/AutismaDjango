from django.db.models import Q # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User,Child,Image,Game
from django.core.exceptions import ValidationError
from uuid import uuid4


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(max_length=8)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )


class UserLoginSerializer(serializers.ModelSerializer):
    # to accept either username or email
    user_id = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        # user,email,password validator
        user_id = data.get("user_id", None)
        password = data.get("password", None)
        if not user_id and not password:
            raise ValidationError("Details not entered.")
        user = None
        # if the email has been passed
        if '@' in user_id:
            user = User.objects.filter(
                Q(email=user_id) &
                Q(password=password)
                ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(email=user_id)
        else:
            user = User.objects.filter(
                Q(username=user_id) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(username=user_id)
        if user.ifLogged:
            raise ValidationError("User already logged in.")
        user.ifLogged = True
        data['token'] = uuid4()
        user.token = data['token']
        user.save()
        return data

    class Meta:
        model = User
        fields = (
            'user_id',
            'password',
            'token',
        )

        read_only_fields = (
            'token',
        )

class ChildLoginSerializer(serializers.ModelSerializer):
    # to accept either username or email
    user_id = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        # user,email,password validator
        user_id = data.get("user_id", None)
        password = data.get("password", None)
        if not user_id and not password:
            raise ValidationError("Details not entered.")
        user = None
        # if the email has been passed
        if '@' in user_id:
            user = Child.objects.filter(
                Q(email=user_id) &
                Q(password=password)
                ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = Child.objects.get(email=user_id)
        else:
            user = Child.objects.filter(
                Q(cname=user_id) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = Child.objects.get(cname=user_id)
        user.ifLogged = True
        data['token'] = uuid4()
        user.token = data['token']
        user.save()
        return data

    class Meta:
        model = User
        fields = (
            'user_id',
            'password',
            'token',
        )

        read_only_fields = (
            'token',
        )
class UserLogoutSerializer(serializers.ModelSerializer):
    token = serializers.CharField()
    status = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        token = data.get("token", None)
        print(token)
        user = None
        try:
            user = User.objects.get(token=token)
            if not user.ifLogged:
                raise ValidationError("User is not logged in.")
        except Exception as e:
            raise ValidationError(str(e))
        user.ifLogged = False
        user.token = ""
        user.save()
        data['status'] = "User is logged out."
        return data

    class Meta:
        model = User
        fields = (
            'token',
            'status',
        )

class ChildSerializer(serializers.ModelSerializer):
    cname = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Child.objects.all())]
        )
    password = serializers.CharField(max_length=8)

    class Meta:
        model = Child
        fields = (
            'cname',
            'password'
        ) 

class ImageSerializer(serializers.ModelSerializer):
    image1 = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Image.objects.all())]
        )
    voice = serializers.CharField(max_length=100)

    class Meta:
        model = Image
        fields = (
            'image1',
            'voice'
        )                


class GameSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Game.objects.all())]
        )
    score = serializers.CharField(max_length=100)
    

    class Meta:
        model = Child
        fields = (
            'name',
            'score',
            

        )