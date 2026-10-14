import os
import urllib.request
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Category, Product

media_dir = os.path.join(os.path.dirname(__file__), 'media')
products_dir = os.path.join(media_dir, 'products')
categories_dir = os.path.join(media_dir, 'categories')

os.makedirs(products_dir, exist_ok=True)
os.makedirs(categories_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def download_image(url, filepath):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Successfully downloaded: {os.path.basename(filepath)}")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

category_images = {
    "Electronics": "https://images.unsplash.com/photo-1498049794561-7780e7231661?q=80&w=800&auto=format&fit=crop",
    "Clothing": "https://images.unsplash.com/photo-1489987707025-afc232f7ea0f?q=80&w=800&auto=format&fit=crop",
    "Home & Kitchen": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?q=80&w=800&auto=format&fit=crop",
    "Sports & Outdoors": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?q=80&w=800&auto=format&fit=crop",
    "Books": "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?q=80&w=800&auto=format&fit=crop",
    "Beauty & Personal Care": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?q=80&w=800&auto=format&fit=crop",
}

for cat_name, img_url in category_images.items():
    cat = Category.objects.filter(name=cat_name).first()
    if cat:
        filename = f"{cat.slug}.jpg"
        filepath = os.path.join(categories_dir, filename)
        if download_image(img_url, filepath):
            cat.image = f"categories/{filename}"
            cat.save()

product_images = {
    "Wireless Bluetooth Headphones": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=800&auto=format&fit=crop",
    "Smart Watch Pro": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=800&auto=format&fit=crop",
    "Portable Bluetooth Speaker": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?q=80&w=800&auto=format&fit=crop",
    "USB-C Fast Charger": "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?q=80&w=800&auto=format&fit=crop",
    "Wireless Mouse": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?q=80&w=800&auto=format&fit=crop",

    "Classic Denim Jacket": "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?q=80&w=800&auto=format&fit=crop",
    "Premium Cotton T-Shirt": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?q=80&w=800&auto=format&fit=crop",
    "Running Sneakers": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=800&auto=format&fit=crop",
    "Leather Belt": "https://images.unsplash.com/photo-1624222247344-550fb60583dc?q=80&w=800&auto=format&fit=crop",
    "Wool Blend Scarf": "https://images.unsplash.com/photo-1520903920243-00d872a2d1c9?q=80&w=800&auto=format&fit=crop",

    "Stainless Steel Water Bottle": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?q=80&w=800&auto=format&fit=crop",
    "Non-Stick Cookware Set": "https://images.unsplash.com/photo-1584992236310-6edddc08acff?q=80&w=800&auto=format&fit=crop",
    "Aromatherapy Diffuser": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?q=80&w=800&auto=format&fit=crop",
    "Bamboo Cutting Board Set": "https://images.unsplash.com/photo-1590794056226-77ef3a6c474e?q=80&w=800&auto=format&fit=crop",

    "Yoga Mat Premium": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?q=80&w=800&auto=format&fit=crop",
    "Resistance Bands Set": "https://images.unsplash.com/photo-1598289431512-b97b0917affc?q=80&w=800&auto=format&fit=crop",
    "Hiking Backpack 40L": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?q=80&w=800&auto=format&fit=crop",
    "Jump Rope Speed Cable": "https://images.unsplash.com/photo-1599058945522-28d584b6f0ff?q=80&w=800&auto=format&fit=crop",

    "The Art of Programming": "https://images.unsplash.com/photo-1532012197267-da84d127e765?q=80&w=800&auto=format&fit=crop",
    "Mindful Leadership": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?q=80&w=800&auto=format&fit=crop",
    "Digital Marketing Guide": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800&auto=format&fit=crop",
    "Creative Writing Handbook": "https://images.unsplash.com/photo-1455390582262-044cdead277a?q=80&w=800&auto=format&fit=crop",

    "Organic Face Serum": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?q=80&w=800&auto=format&fit=crop",
    "Natural Hair Care Set": "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?q=80&w=800&auto=format&fit=crop",
    "Essential Oils Collection": "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?q=80&w=800&auto=format&fit=crop",
    "Bamboo Toothbrush Set": "https://images.unsplash.com/photo-1607613009820-a29f7bb81c04?q=80&w=800&auto=format&fit=crop"
}

for prod_name, img_url in product_images.items():
    prod = Product.objects.filter(name=prod_name).first()
    if prod:
        filename = f"{prod.slug}.jpg"
        filepath = os.path.join(products_dir, filename)
        if download_image(img_url, filepath):
            prod.image = f"products/{filename}"
            prod.save()

print("Original product photos downloaded!")
