import os
import django
from django.utils.text import slugify
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import Category, Product

def run():
    print("Starting database seed...")

    # Create Superuser
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@codealpha.com', 'admin123')
        print("Created superuser: admin")
    else:
        print("Superuser admin already exists")

    # Categories data
    categories_data = [
        "Electronics", 
        "Clothing", 
        "Home & Kitchen", 
        "Sports & Outdoors", 
        "Books", 
        "Beauty & Personal Care"
    ]
    
    category_objects = {}
    for cat_name in categories_data:
        cat, created = Category.objects.get_or_create(
            name=cat_name, 
            defaults={'slug': slugify(cat_name)}
        )
        category_objects[cat_name] = cat
        if created:
            print(f"Created category: {cat_name}")

    # Products data
    products_data = [
        # Electronics
        {"name": "Wireless Bluetooth Headphones", "price": 79.99, "compare_price": 129.99, "category": "Electronics", "is_featured": True, "desc": "High quality sound with noise cancellation. Perfect for everyday use."},
        {"name": "Smart Watch Pro", "price": 199.99, "compare_price": 299.99, "category": "Electronics", "is_featured": True, "desc": "Track your fitness and stay connected on the go."},
        {"name": "Portable Bluetooth Speaker", "price": 49.99, "compare_price": None, "category": "Electronics", "is_featured": True, "desc": "Waterproof portable speaker with 12 hours of battery life."},
        {"name": "USB-C Fast Charger", "price": 24.99, "compare_price": 39.99, "category": "Electronics", "is_featured": False, "desc": "Fast charging adapter for all your devices."},
        {"name": "Wireless Mouse", "price": 29.99, "compare_price": None, "category": "Electronics", "is_featured": False, "desc": "Ergonomic wireless mouse with precision tracking."},
        
        # Clothing
        {"name": "Classic Denim Jacket", "price": 89.99, "compare_price": 129.99, "category": "Clothing", "is_featured": True, "desc": "A timeless classic denim jacket for any casual outfit."},
        {"name": "Premium Cotton T-Shirt", "price": 29.99, "compare_price": None, "category": "Clothing", "is_featured": True, "desc": "Ultra-soft 100% cotton t-shirt. Available in multiple colors."},
        {"name": "Running Sneakers", "price": 119.99, "compare_price": 159.99, "category": "Clothing", "is_featured": False, "desc": "Lightweight and breathable sneakers for your daily run."},
        {"name": "Leather Belt", "price": 34.99, "compare_price": None, "category": "Clothing", "is_featured": False, "desc": "Genuine leather belt with a classic buckle design."},
        {"name": "Wool Blend Scarf", "price": 39.99, "compare_price": None, "category": "Clothing", "is_featured": False, "desc": "Keep warm and stylish with this premium wool blend scarf."},

        # Home & Kitchen
        {"name": "Stainless Steel Water Bottle", "price": 19.99, "compare_price": None, "category": "Home & Kitchen", "is_featured": True, "desc": "Double-wall insulated water bottle. Keeps drinks cold for 24 hours."},
        {"name": "Non-Stick Cookware Set", "price": 149.99, "compare_price": 199.99, "category": "Home & Kitchen", "is_featured": True, "desc": "Complete 10-piece cookware set. Easy to clean and durable."},
        {"name": "Aromatherapy Diffuser", "price": 34.99, "compare_price": None, "category": "Home & Kitchen", "is_featured": False, "desc": "Create a relaxing atmosphere in your home with this sleek diffuser."},
        {"name": "Bamboo Cutting Board Set", "price": 29.99, "compare_price": None, "category": "Home & Kitchen", "is_featured": False, "desc": "Eco-friendly bamboo cutting boards in three versatile sizes."},

        # Sports & Outdoors
        {"name": "Yoga Mat Premium", "price": 39.99, "compare_price": None, "category": "Sports & Outdoors", "is_featured": True, "desc": "Non-slip premium yoga mat with alignment lines."},
        {"name": "Resistance Bands Set", "price": 24.99, "compare_price": 34.99, "category": "Sports & Outdoors", "is_featured": False, "desc": "Set of 5 resistance bands for a full body workout anywhere."},
        {"name": "Hiking Backpack 40L", "price": 69.99, "compare_price": 99.99, "category": "Sports & Outdoors", "is_featured": False, "desc": "Durable and water-resistant backpack for your outdoor adventures."},
        {"name": "Jump Rope Speed Cable", "price": 14.99, "compare_price": None, "category": "Sports & Outdoors", "is_featured": False, "desc": "Adjustable speed jump rope for cardio fitness training."},

        # Books
        {"name": "The Art of Programming", "price": 49.99, "compare_price": None, "category": "Books", "is_featured": False, "desc": "A comprehensive guide to mastering software development."},
        {"name": "Mindful Leadership", "price": 24.99, "compare_price": None, "category": "Books", "is_featured": False, "desc": "Strategies for leading with emotional intelligence and focus."},
        {"name": "Digital Marketing Guide", "price": 34.99, "compare_price": 44.99, "category": "Books", "is_featured": False, "desc": "Everything you need to know to grow your business online."},
        {"name": "Creative Writing Handbook", "price": 19.99, "compare_price": None, "category": "Books", "is_featured": False, "desc": "Unlock your creativity and improve your writing skills."},

        # Beauty & Personal Care
        {"name": "Organic Face Serum", "price": 42.99, "compare_price": 59.99, "category": "Beauty & Personal Care", "is_featured": False, "desc": "Rejuvenate your skin with our all-natural, organic face serum."},
        {"name": "Natural Hair Care Set", "price": 54.99, "compare_price": None, "category": "Beauty & Personal Care", "is_featured": False, "desc": "Shampoo and conditioner set made with natural botanical extracts."},
        {"name": "Essential Oils Collection", "price": 29.99, "compare_price": None, "category": "Beauty & Personal Care", "is_featured": False, "desc": "A curated collection of our most popular essential oils."},
        {"name": "Bamboo Toothbrush Set", "price": 12.99, "compare_price": None, "category": "Beauty & Personal Care", "is_featured": False, "desc": "Eco-friendly bamboo toothbrushes. Pack of 4."},
    ]

    for p_data in products_data:
        cat = category_objects[p_data["category"]]
        prod, created = Product.objects.get_or_create(
            name=p_data["name"],
            defaults={
                'slug': slugify(p_data["name"]),
                'description': p_data["desc"],
                'price': p_data["price"],
                'compare_price': p_data.get("compare_price"),
                'stock': random.randint(5, 50),
                'category': cat,
                'is_featured': p_data["is_featured"],
                'is_active': True
            }
        )
        if created:
            print(f"Created product: {prod.name}")

    print("Database seeding completed successfully!")

if __name__ == '__main__':
    run()
