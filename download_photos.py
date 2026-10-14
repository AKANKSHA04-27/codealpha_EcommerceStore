import os
import urllib.request
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Category, Product

# Create media directories if they don't exist
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

# Category images mapping
category_images = {
    "Haute Horlogerie": "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?q=80&w=800&auto=format&fit=crop",
    "Designer Apparel": "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?q=80&w=800&auto=format&fit=crop",
    "Fine Jewelry": "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?q=80&w=800&auto=format&fit=crop",
    "Leather Goods": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?q=80&w=800&auto=format&fit=crop",
    "Artisanal Fragrance": "https://images.unsplash.com/photo-1594035910387-fea47794261f?q=80&w=800&auto=format&fit=crop",
    "Luxury Home": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?q=80&w=800&auto=format&fit=crop",
}

for cat_name, img_url in category_images.items():
    cat = Category.objects.filter(name=cat_name).first()
    if cat:
        filename = f"{cat.slug}.jpg"
        filepath = os.path.join(categories_dir, filename)
        if download_image(img_url, filepath):
            cat.image = f"categories/{filename}"
            cat.save()

# Product images mapping
product_images = {
    "Chronograph Tourbillon Platinum Edition": "https://images.unsplash.com/photo-1524805444758-089113d48a6d?q=80&w=800&auto=format&fit=crop",
    "Royal Oak Perpetual Calendar Rose Gold": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=800&auto=format&fit=crop",
    "Submariner Automatic Diver Spec-1": "https://images.unsplash.com/photo-1539185441755-769473a23570?q=80&w=800&auto=format&fit=crop",
    "Vintage Skeleton GMT Automatic": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?q=80&w=800&auto=format&fit=crop",

    "Silk Cashmere Trench Overcoat": "https://images.unsplash.com/photo-1539533018447-63fcce2678e3?q=80&w=800&auto=format&fit=crop",
    "Velvet Evening Tuxedo Jacket": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=800&auto=format&fit=crop",
    "Hand-Woven Merino Wool Blazer": "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?q=80&w=800&auto=format&fit=crop",
    "Pure Silk Plunge Evening Gown": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?q=80&w=800&auto=format&fit=crop",

    "Solitaire Diamond Pendant in 18k Gold": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?q=80&w=800&auto=format&fit=crop",
    "Emerald & Diamond Halo Ring": "https://images.unsplash.com/photo-1605100804763-247f67b3557e?q=80&w=800&auto=format&fit=crop",
    "South Sea Pearl & Diamond Earrings": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?q=80&w=800&auto=format&fit=crop",

    "Full-Grain Italian Calfskin Tote": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=800&auto=format&fit=crop",
    "Structured Crossbody Bag Gold Hardware": "https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?q=80&w=800&auto=format&fit=crop",
    "Monogrammed All-Travel Duffle": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?q=80&w=800&auto=format&fit=crop",

    "Oud & Royal Rose Extrait de Parfum 100ml": "https://images.unsplash.com/photo-1541643600914-78b084683601?q=80&w=800&auto=format&fit=crop",
    "Velvet Amber & Vanilla Absolute 50ml": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?q=80&w=800&auto=format&fit=crop",

    "Hand-Blown Crystal Decanter Set": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?q=80&w=800&auto=format&fit=crop",
    "Egyptian Cotton 1000TC Sheet Set": "https://images.unsplash.com/photo-1631679706909-1844bbd07221?q=80&w=800&auto=format&fit=crop"
}

for prod_name, img_url in product_images.items():
    prod = Product.objects.filter(name=prod_name).first()
    if prod:
        filename = f"{prod.slug}.jpg"
        filepath = os.path.join(products_dir, filename)
        if download_image(img_url, filepath):
            prod.image = f"products/{filename}"
            prod.save()

print("All product & category images downloaded and updated successfully!")
