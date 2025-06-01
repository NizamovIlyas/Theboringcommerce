from django.urls import path
from .api_endpoints import (
    ProductListView, ProductCreateView, ProductGetView,
    ProductUpdateView, ProductDeleteView,
    BrandCreateView,
    ColourCreateView, ColourListView,
    SizeCreateView, SizeListView,
    ProductVariantCreateView, ProductVariantDetailView,
    ProductVariantListView, ProductVariantUpdateView,
    ProductVariantDeleteView, ProductVariantListByProductView,
)

urlpatterns = [
    # Product
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<slug:slug>/', ProductGetView.as_view(), name='product-detail'),
    path('products/<slug:slug>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<slug:slug>/delete/', ProductDeleteView.as_view(), name='product-delete'),

    # Brand
    # path('brands/', BrandListView.as_view(), name='brand-list'),
    path('brands/create/', BrandCreateView.as_view(), name='brand-create'),

    # Colour
    path('colours/', ColourListView.as_view(), name='colour-list'),
    path('colours/create/', ColourCreateView.as_view(), name='colour-create'),

    # Size
    path('sizes/', SizeListView.as_view(), name='size-list'),
    path('sizes/create/', SizeCreateView.as_view(), name='size-create'),

    # Product Variant
    path('variants/', ProductVariantListView.as_view(), name='variant-list'),
    path('variants/create/', ProductVariantCreateView.as_view(), name='variant-create'),
    path('variants/<int:pk>/', ProductVariantDetailView.as_view(), name='variant-detail'),
    path('variants/<int:pk>/update/', ProductVariantUpdateView.as_view(), name='variant-update'),
    path('variants/<int:pk>/delete/', ProductVariantDeleteView.as_view(), name='variant-delete'),
    path('products/<slug:slug>/variants/', ProductVariantListByProductView.as_view(), name='variants-by-product'),
]
