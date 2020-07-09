from django.urls import path, re_path
from . import views

urlpatterns = [
    path('collections/<str:category>', views.return_category_collection,
         name='category_collection'),
    path('products/<str:product>', views.return_product, name='product'),
    path('cart', views.cart, name='cart'),
    path('cart/<str:product_name>/delete', views.delete_item_from_cart,
         name="cart_item_deletion"),
]
