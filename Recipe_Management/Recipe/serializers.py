from rest_framework import serializers
from Recipe.models import Cuisine
from django.contrib.auth.models import User


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cuisine
        fields=['id','Title','Meal','Ingredients','Rating','Review']



class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['id','username','password']

    def create(self,validated_data):
        u=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
        return u

