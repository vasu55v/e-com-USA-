from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password","date_joined"]
        extra_kwargs={
            "password":{"write_only":True},         
                      }


        def create(self,**validated_data):
            user=User.objects.create(**validated_data)
            return user
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=address
        fields="__all__"

        def create(self,**validated_data):
            adrs=address.objects.create(**validated_data)
            return adrs

class ProductSerializer(serializers.ModelSerializer):

    # seller = serializers.SerializerMethodField()

    # def get_seller(self, obj):
    #     return obj.seller
    
    class Meta:
        model=product
        fields=["name","description","price","image","category"]

        def create(self,**validated_data):
            prod=product.objects.create(**validated_data)
            return prod

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=cart
        fields="__all__"
        extra_kwargs={"password":{"write_only":True}}

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=customer
        fields="__all__"
        extra_kwargs={
            "password":{"write_only":True}
            }


        def create(self,**validated_data):
            cus=customer.object.create(**validated_data)
            return cus
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"

        def create(self,**validated_data):
            odr=Order.object.create(**validated_data)
            return odr
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields="__all__"