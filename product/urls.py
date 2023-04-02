from django.urls import path

from product.views import ProductView, ProductCreate, ProductUpdate

urlpatterns = [
    path('', ProductView.as_view(), name='product'),
    path('product_create/', ProductCreate.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdate.as_view(), name='product_update')
]
