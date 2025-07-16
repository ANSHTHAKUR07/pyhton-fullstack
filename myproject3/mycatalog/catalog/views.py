from django.http import HttpResponse
from .models import Product

def operations(request):
    # 1. CREATE
    Product.objects.create(name='Phone', description='Smartphone', price=999.99, stock=10)

    # 2. SELECT ALL
    all_products = Product.objects.all()

    # 3. GET FIRST (Get product with id=1)
    try:
        one_product = Product.objects.get(id=1)
    except Product.DoesNotExist:
        one_product = None

    # 4. FILTER
    cheap_products = Product.objects.filter(price__lt=1000)

    # 5. UPDATE (Save)
    if one_product:
        one_product.price = 899.99
        one_product.save()

    # 6. DELETE
    if one_product:
        one_product.delete()

    return HttpResponse("CRUD operations completed. Check database.")
from django.http import HttpResponse
from .models import Product

def operations(request):
    return HttpResponse("Product catalog operations loaded successfully!")
