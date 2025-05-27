from django.views.generic import TemplateView,  ListView
from django.db.models import Q, Min, Max
from products.models import ProductVariant, Category, Color, Size, Product



class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all()

        context['title'] = 'BoringCommerce | Home'
        context['categories'] = categories
        return context
    

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BoringCommerce | Contact Us'
        return context
    

class CheckoutView(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BoringCommerce | Checkout'
        return context
    

class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BoringCommerce | Checkout'
        return context
    


class ShopGridView(ListView):
    model = ProductVariant
    template_name = 'shop-grid.html'
    context_object_name = 'variants'
    paginate_by = 9

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        sort = self.request.GET.get('sort')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        colors = self.request.GET.getlist('colors')
        sizes = self.request.GET.getlist('sizes')

        queryset = queryset.filter(is_active=True, product__is_active=True)


        if query:
            queryset = queryset.filter(
                Q(product__name__icontains=query) | Q(product__description__icontains=query)
            )

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)

        if colors:
            queryset = queryset.filter(color__slug__in=colors)

        if sizes:
            queryset = queryset.filter(size__slug__in=sizes)


        if sort == 'price_asc':
            queryset = queryset.order_by('price')
        elif sort == 'price_desc':
            queryset = queryset.order_by('-price')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['latest_products'] = Product.objects.order_by('-created_at')[:6]


        # Dynamic filter options
        context['colors'] = Color.objects.filter(product_variants__isnull=False).distinct().order_by('name')
        context['colors'] = [item['color'] for item in context['colors']]
        context['sizes'] = Size.objects.filter(product_variants__isnull=False).distinct().order_by('name')
        context['sizes'] = [item['size'] for item in context['sizes']]
        
        # Price range
        price_range = ProductVariant.objects.aggregate(min_price=Min('price'), max_price=Max('price'))
        context['min_price'] = int(price_range['min_price']) if price_range['min_price'] else 10
        context['max_price'] = int(price_range['max_price']) if price_range['max_price'] else 540
        
        # Selected filters
        context['selected_colors'] = self.request.GET.getlist('colors')
        context['selected_sizes'] = self.request.GET.getlist('sizes')
        
        return context
    

class ShopingCartView(TemplateView):
    template_name = 'shoping-cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'BoringCommerce | Checkout'
        return context
    