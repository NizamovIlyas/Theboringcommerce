from .ProductCRUD import (
    ProductCreateView,
    ProductDeleteView,
    ProductUpdateView, 
    ProductListView, 
    ProductGetView,
    )

from .BrandCRUD import (
    BrandCreateView,
    # BrandListView,
)

from .ColourCRUD import (
    ColourCreateView,
    ColourListView
)

from .SizeCRUD import (
    SizeCreateView,
    SizeListView,
)

from .ProductVariantCRUD import (
    ProductVariantCreateView,
    ProductVariantDetailView,
    ProductVariantListView,
    ProductVariantUpdateView,
    ProductVariantDeleteView,
    ProductVariantListByProductView,
)

__all__ = [
    # Product CRUD
    'ProductCreateView', 
    'ProductDeleteView',
    'ProductUpdateView',
    'ProductListView', 
    'ProductGetView',

    # Brand CRUD
    'BrandCreateView', 
    'BrandListView',
    # Colour CRUD
    'ColourCreateView',
    'ColourListView',

    # Size CRUD
    'SizeCreateView',
    'SizeListView', 
    # ProductVariant CRUD
    'ProductVariantCreateView',
    'ProductVariantDetailView',
    'ProductVariantListView',
    'ProductVariantUpdateView',
    'ProductVariantDeleteView',
    'ProductVariantListByProductView',
]
