import os
import urllib.request
import django
from concurrent.futures import ThreadPoolExecutor

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Category, Product

media_dir = os.path.join(os.path.dirname(__file__), 'media')
products_dir = os.path.join(media_dir, 'products')
categories_dir = os.path.join(media_dir, 'categories')

os.makedirs(products_dir, exist_ok=True)
os.makedirs(categories_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

category_images = {
    "Electronics & Gadgets": "https://images.unsplash.com/photo-1498049794561-7780e7231661?q=80&w=800&auto=format&fit=crop",
    "Designer Apparel": "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?q=80&w=800&auto=format&fit=crop",
    "Fine Jewelry & Watches": "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?q=80&w=800&auto=format&fit=crop",
    "Leather Goods": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?q=80&w=800&auto=format&fit=crop",
    "Artisanal Fragrance": "https://images.unsplash.com/photo-1594035910387-fea47794261f?q=80&w=800&auto=format&fit=crop",
    "Luxury Home": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?q=80&w=800&auto=format&fit=crop",
    "Sports & Outdoors": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?q=80&w=800&auto=format&fit=crop",
    "Books & Stationery": "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?q=80&w=800&auto=format&fit=crop"
}

def process_category(cat_name_img):
    cat_name, img_url = cat_name_img
    cat = Category.objects.filter(name=cat_name).first()
    if cat:
        filename = f"{cat.slug}.jpg"
        filepath = os.path.join(categories_dir, filename)
        try:
            req = urllib.request.Request(img_url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp, open(filepath, 'wb') as f:
                f.write(resp.read())
            cat.image = f"categories/{filename}"
            cat.save()
            print(f"Downloaded category image: {cat_name}")
        except Exception as e:
            print(f"Error category {cat_name}: {e}")

with ThreadPoolExecutor(max_workers=8) as executor:
    executor.map(process_category, category_images.items())

print("Category images updated. Now downloading product images...")
