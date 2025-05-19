from .ProductCRUD import (
    ProductCreateView, ProductCreateSerializer,
    ProductDeleteView,
    ProductUpdateView, ProductUpdateSerializer,
    ProductListView, ProductListSerializer,
    ProductGetView, ProductGetSerializer,
)

from .BrandCRUD import (
    BrandCreateView, BrandCreateSerializer,
    BrandListView, BrandListSerializer,
)

from .ColourCRUD import (
    ColourCreateView, ColourCreateSerializer,
    ColourListView, ColourListSerializer,
)

from .SizeCRUD import (
    SizeCreateView, SizeCreateSerializer,
    SizeListView, SizeListSerializer,
)

from .ProductVariantCRUD import (
    ProductVariantCreateView, ProductVariantCreateSerializer,
    ProductVariantDetailView, ProductVariantGetSerializer,
    ProductVariantListView, ProductVariantListSerializerForList,
    ProductVariantUpdateView, ProductVariantUpdateSerializer,
    ProductVariantDeleteView,
    ProductVariantListByProductView,
)

__all__ = [
    # Product CRUD
    'ProductCreateView', 'ProductCreateSerializer',
    'ProductDeleteView',
    'ProductUpdateView', 'ProductUpdateSerializer',
    'ProductListView', 'ProductListSerializer',
    'ProductGetView', 'ProductGetSerializer',

    # Brand CRUD
    'BrandCreateView', 'BrandCreateSerializer',
    'BrandListView', 'BrandListSerializer',

    # Colour CRUD
    'ColourCreateView', 'ColourCreateSerializer',
    'ColourListView', 'ColourListSerializer',

    # Size CRUD
    'SizeCreateView', 'SizeCreateSerializer',
    'SizeListView', 'SizeListSerializer',

    # ProductVariant CRUD
    'ProductVariantCreateView', 'ProductVariantCreateSerializer',
    'ProductVariantDetailView', 'ProductVariantGetSerializer',
    'ProductVariantListView', 'ProductVariantListSerializerForList',
    'ProductVariantUpdateView', 'ProductVariantUpdateSerializer',
    'ProductVariantDeleteView',
    'ProductVariantListByProductView', 'ProductVariantListSerializerByProduct'
]
