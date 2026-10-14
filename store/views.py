from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from .models import Category, Product, Cart, CartItem, Order, OrderItem
from .forms import CheckoutForm

def _get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        if not request.session.session_key:
            request.session.create()
        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart

def home(request):
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:8]
    categories = Category.objects.all()[:6]
    return render(request, 'store/home.html', {
        'featured_products': featured_products,
        'categories': categories
    })

def product_list(request):
    products = Product.objects.filter(is_active=True)
    category_slug = request.GET.get('category')
    current_category = None
    
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)
        
    search_query = request.GET.get('q')
    if search_query:
        products = products.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
        
    sort_by = request.GET.get('sort')
    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    elif sort_by == 'newest':
        products = products.order_by('-created_at')
    elif sort_by == 'name':
        products = products.order_by('name')
        
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'store/product_list.html', {
        'products': page_obj,
        'categories': Category.objects.all(),
        'current_category': current_category,
        'search_query': search_query,
        'sort_by': sort_by,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category, is_active=True).exclude(id=product.id)[:4]
    return render(request, 'store/product_detail.html', {
        'product': product,
        'related_products': related_products
    })

@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart = _get_or_create_cart(request)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    
    messages.success(request, f"{product.name} added to cart.")
    return redirect('store:cart')

def cart_detail(request):
    cart = _get_or_create_cart(request)
    cart_items = cart.items.select_related('product').all()
    return render(request, 'store/cart.html', {
        'cart': cart,
        'cart_items': cart_items,
        'cart_total': cart.total
    })

@require_POST
def update_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    quantity = int(request.POST.get('quantity', 0))
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, "Cart updated.")
    else:
        cart_item.delete()
        messages.success(request, "Item removed from cart.")
    return redirect('store:cart')

@require_POST
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect('store:cart')

@login_required
def checkout(request):
    cart = _get_or_create_cart(request)
    cart_items = cart.items.select_related('product').all()
    
    if not cart_items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect('store:product_list')
        
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                zip_code=form.cleaned_data['zip_code'],
                total=cart.total
            )
            
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
                item.product.stock -= item.quantity
                item.product.save()
                
            cart_items.delete()
            messages.success(request, "Order placed successfully.")
            return redirect('store:order_confirmation', order_number=order.order_number)
    else:
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
        # Pre-fill from user profile if available
        try:
            profile = request.user.profile
            initial_data.update({
                'phone': profile.phone,
                'address': profile.address,
                'city': profile.city,
                'state': profile.state,
                'zip_code': profile.zip_code,
            })
        except Exception:
            pass
        form = CheckoutForm(initial=initial_data)
        
    return render(request, 'store/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'cart_total': cart.total
    })

@login_required
def order_confirmation(request, order_number):
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    return render(request, 'store/order_confirmation.html', {
        'order': order
    })
