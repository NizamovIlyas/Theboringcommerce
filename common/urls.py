from django.urls import path

from common.views import HomeView, ContactView, CheckoutView, BlogView, ShopGridView, ShopingCartView, BlogDetailsView, ShopDetailsView



app_name = "common"

urlpatterns = [
    path("index/", HomeView.as_view(), name="index"),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path("contact/", ContactView.as_view(), name="contact"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("shopgrid/", ShopGridView.as_view(), name="shop-grid"),
    path("shopingcart/", ShopingCartView.as_view(), name="shoping-cart"),
    path("blogdetails/", BlogDetailsView.as_view(), name="blog-details"),
    path("shopdetails/", ShopDetailsView.as_view(), name="shop-details"),
]
