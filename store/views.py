from django.shortcuts import get_object_or_404, render

from .models import Category, Product

# def categories(request):
#     return {
#         'categories': Category.objects.all()
#     }

def all_products(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, 'store/index.html', {'products': products})
# store/index.html --> vine din templates

# SLUG again
# ca si cum am folosi acel cuvant din url(aparut pe baza slug)
# pentru a face un fel de query in baza de date
def product_detail(request, slug, is_active=True):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/single.html', {'product': product})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)  #asta va returna un obiect din categoria vizata(get_object_or_404)
    products = Product.objects.filter(
        category__in = category.get_descendants(include_self=True)
    )
    return render(request, 'store/category.html', {'category': category, 'products': products})

# def subcategory_list(request, subcategory_slug=None):
#     category = get_object_or_404(Category, slug=subcategory_slug)  #asta va returna un obiect din categoria vizata(get_object_or_404)
#     subcategory = Subcategory.objects.filter(category=category)
#     products = Product.objects.filter(subcategory=subcategory)
#     return render(request, 'products/subcategory_list.html', {'subcategory': subcategory, 'products': products})

