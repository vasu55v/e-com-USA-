from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import *
from rest_framework.authentication import TokenAuthentication


class CreateUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes =[AllowAny]

class CreateCustomerView(generics.CreateAPIView):
    serializer_class=CustomerSerializer
    permission_classes =[AllowAny]

    def get_queryset(self):
        return customer.objects.all()

class CustomerView(generics.ListAPIView):
    queryset=customer.objects.all()
    serializer_class=CustomerSerializer
    permission_classes =[IsAuthenticated,TokenAuthentication]

class DeleteCustomer(generics.DestroyAPIView):
    queryset=customer.objects.all()
    serializer_class=CustomerSerializer
    permission_classes =[IsAuthenticated]

    # def get_queryset(self):
    #     user=self.request.User
    #     return cart.objects.filter(username=user)


class ProductView(generics.ListAPIView):
    queryset=product.objects.all()
    serializer_class=ProductSerializer
    permission_classes =[AllowAny]

class CreateProductView(generics.CreateAPIView):
    serializer_class=ProductSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        return product.objects.all()
    
    def perform_create(self,serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user) 
        else:
            print(serializer.errors)

class DeleteProduct(generics.DestroyAPIView):
    serializer_class=ProductSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        return product.objects.filter(user=self.request.User)
    

class CreateCartItem(generics.CreateAPIView):
    serializer_class=CartSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        user=self.request.User
        return cart.objects.create(customer=user)


class GetCartItem(generics.ListAPIView):
    serializer_class=CartSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        user=self.request.User
        return cart.objects.filter(customer=user)
    

class DeleteCartItem(generics.DestroyAPIView):
    serializer_class=CartSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user = self.request.User
        return cart.objects.filter(customer=user)

   
class CreateOrderItem(generics.CreateAPIView):
    serializer_class=OrderSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        user=self.request.User
        return cart.objects.all()


class GetOrderItem(generics.ListAPIView):
    serializer_class=OrderSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        user=self.request.User
        return cart.objects.filter(customer=user)
    
 

class DeleteOrderItem(generics.DestroyAPIView):
    serializer_class=OrderSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        user=self.request.User
        return cart.objects.filter(customer=user)
    
       
    



    

    



