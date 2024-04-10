from django.urls import path
from . import views

urlpatterns = [
    # path('user/',views.CreateUserView.as_view(),name="customer"),
    path('customer/',views.CustomerView.as_view(),name="customer"),
    path('customer/create/',views.CreateCustomerView.as_view(),name="create_customer"),
    path('customer/delete/<int:pk>/',views.DeleteCustomer.as_view(),name="delete_customer"),

    path('product/',views.ProductView.as_view(),name="product"),
    path('product/create/',views.CreateProductView.as_view(),name="create_product"),
    path('product/delete/<int:pk>/',views.DeleteProduct.as_view(),name="delete_product"),

    path('cart/',views.GetCartItem.as_view(),name="cart"),
    path('cart/create/',views.CreateCartItem.as_view(),name="create_cart"),
    path('cart/delete/<int:pk>/',views.DeleteCartItem.as_view(),name="delete_cart"),
    
    path('order/',views.GetOrderItem.as_view(),name="order"),
    path('order/create/',views.CreateOrderItem.as_view(),name="create_order"),
    path('order/delete/<int:pk>/',views.DeleteOrderItem.as_view(),name="delete_order"),

]
