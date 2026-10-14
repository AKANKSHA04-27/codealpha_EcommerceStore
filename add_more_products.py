import os
import urllib.request
import random
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from store.models import Category, Product

media_dir = os.path.join(os.path.dirname(__file__), 'media')
products_dir = os.path.join(media_dir, 'products')
os.makedirs(products_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def download_image(url, filepath):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded: {os.path.basename(filepath)}")
        return True
    except Exception as e:
        print(f"Failed {url}: {e}")
        return False

new_products = [
    # Haute Horlogerie
    {"name": "Grand Complication Perpetual Calendar", "price": 9500.00, "compare_price": 1100.00, "category": "Haute Horlogerie", "is_featured": True, "desc": "Astronomical precision timepiece with moonphase, leap year indicator, and perpetual calendar mechanism.", "img": "https://images.unsplash.com/photo-1547996160-81dfa63595aa?q=80&w=800&auto=format&fit=crop"},
    {"name": "Rose Gold Skeleton Tourbillon", "price": 6400.00, "compare_price": 7500.00, "category": "Haute Horlogerie", "is_featured": True, "desc": "Hand-engraved 18k rose gold skeletonized movement with 72-hour power reserve.", "img": "https://images.unsplash.com/photo-1526045612212-70caf35c14df?q=80&w=800&auto=format&fit=crop"},
    {"name": "Nautical Master Automatic Diver", "price": 3800.00, "compare_price": None, "category": "Haute Horlogerie", "is_featured": False, "desc": "Titanium case deep-sea diver's watch rated to 500 meters with helium escape valve.", "img": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?q=80&w=800&auto=format&fit=crop"},

    # Designer Apparel
    {"name": "Silk Velvet Dinner Jacket", "price": 1280.00, "compare_price": 1600.00, "category": "Designer Apparel", "is_featured": True, "desc": "Rich emerald silk-velvet tuxedo jacket with satin shawl lapels.", "img": "https://images.unsplash.com/photo-1593030761757-71fae45fa0e7?q=80&w=800&auto=format&fit=crop"},
    {"name": "Italian Tailored Wool Coat", "price": 1150.00, "compare_price": None, "category": "Designer Apparel", "is_featured": True, "desc": "Double-breasted long coat in pure virgin wool with horn buttons.", "img": "https://images.unsplash.com/photo-1544441893-675973e31985?q=80&w=800&auto=format&fit=crop"},
    {"name": "Silk Satin Wrap Dress", "price": 890.00, "compare_price": 1100.00, "category": "Designer Apparel", "is_featured": False, "desc": "Fluid drape silk satin dress with waist sash in deep sapphire tone.", "img": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?q=80&w=800&auto=format&fit=crop"},

    # Fine Jewelry
    {"name": "Sapphire & Diamond Cluster Ring", "price": 3400.00, "compare_price": 4100.00, "category": "Fine Jewelry", "is_featured": True, "desc": "Unheated Royal Blue Sri Lankan Sapphire encircled by brilliant marquise diamonds.", "img": "https://images.unsplash.com/photo-1603561591411-07134e71a2a9?q=80&w=800&auto=format&fit=crop"},
    {"name": "Diamond Tennis Bracelet 14k Gold", "price": 2850.00, "compare_price": None, "category": "Fine Jewelry", "is_featured": False, "desc": "Classic 5-carat total weight round brilliant diamond line bracelet in solid 14k gold.", "img": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?q=80&w=800&auto=format&fit=crop"},
    {"name": "Tahitian Black Pearl Necklace", "price": 2200.00, "compare_price": 2600.00, "category": "Fine Jewelry", "is_featured": False, "desc": "Strand of 35 matched peacock-tone Tahitian cultured pearls with 18k gold diamond clasp.", "img": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?q=80&w=800&auto=format&fit=crop"},

    # Leather Goods
    {"name": "Crocodile-Embossed Leather Briefcase", "price": 1650.00, "compare_price": 1950.00, "category": "Leather Goods", "is_featured": True, "desc": "Executive document case in rich cognac crocodile-embossed Italian leather with dual keylocks.", "img": "https://images.unsplash.com/photo-1622560480605-d83c853bc5c3?q=80&w=800&auto=format&fit=crop"},
    {"name": "Suede Fringe Hobo Bag", "price": 780.00, "compare_price": None, "category": "Leather Goods", "is_featured": False, "desc": "Supple calfskin suede shoulder bag with hand-cut fringe details.", "img": "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?q=80&w=800&auto=format&fit=crop"},
    {"name": "Grain Leather Cardholder Wallet", "price": 240.00, "compare_price": 300.00, "category": "Leather Goods", "is_featured": False, "desc": "Slim pocket cardholder with 6 card slots in pebbled French calf leather.", "img": "https://images.unsplash.com/photo-1627123424574-724758594e93?q=80&w=800&auto=format&fit=crop"},

    # Artisanal Fragrance
    {"name": "Imperial Oud & Musk Extrait", "price": 450.00, "compare_price": 520.00, "category": "Artisanal Fragrance", "is_featured": True, "desc": "Concentrated perfume extract featuring aged Assam oud wood, white musk, and Turkish rose.", "img": "https://images.unsplash.com/photo-1592945403244-b3fbafd7f539?q=80&w=800&auto=format&fit=crop"},
    {"name": "Bergamot & Citrus Bloom EDP", "price": 310.00, "compare_price": None, "category": "Artisanal Fragrance", "is_featured": False, "desc": "Sparkling Calabrian bergamot, neroli, and sun-kissed orange blossom fragrance.", "img": "https://images.unsplash.com/photo-1523293182086-7651a899d37f?q=80&w=800&auto=format&fit=crop"},
    {"name": "Smoked Leather & Vetiver Cologne", "price": 340.00, "compare_price": 400.00, "category": "Artisanal Fragrance", "is_featured": False, "desc": "Warm woody cologne with notes of birch tar, Haitian vetiver, and cedarwood.", "img": "https://images.unsplash.com/photo-1615397349754-cfa2066a298e?q=80&w=800&auto=format&fit=crop"},

    # Luxury Home
    {"name": "Marble & Brass Architectural Lamp", "price": 680.00, "compare_price": 820.00, "category": "Luxury Home", "is_featured": True, "desc": "Sculptural desk lamp in Carrara white marble and solid brushed brass.", "img": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?q=80&w=800&auto=format&fit=crop"},
    {"name": "Hand-Carved Oak Wine Cabinet", "price": 1850.00, "compare_price": None, "category": "Luxury Home", "is_featured": False, "desc": "Artisanal solid oak cabinet storing up to 24 reserve bottles with brass hardware.", "img": "https://images.unsplash.com/photo-1513694203232-719a280e022f?q=80&w=800&auto=format&fit=crop"},
    {"name": "Pure Silk Hand-Knotted Area Rug", "price": 2900.00, "compare_price": 3500.00, "category": "Luxury Home", "is_featured": False, "desc": "Intricate Persian-inspired silk area rug hand-knotted over 12 months.", "img": "https://images.unsplash.com/photo-1600121848594-d8644e57abab?q=80&w=800&auto=format&fit=crop"}
]

for p_data in new_products:
    cat = Category.objects.filter(name=p_data["category"]).first()
    if not cat:
        continue
    slug = slugify(p_data["name"])
    filename = f"{slug}.jpg"
    filepath = os.path.join(products_dir, filename)
    
    img_relative = ""
    if download_image(p_data["img"], filepath):
        img_relative = f"products/{filename}"

    prod, created = Product.objects.get_or_create(
        slug=slug,
        defaults={
            'name': p_data["name"],
            'description': p_data["desc"],
            'price': p_data["price"],
            'compare_price': p_data.get("compare_price"),
            'stock': random.randint(8, 25),
            'category': cat,
            'is_featured': p_data["is_featured"],
            'is_active': True,
            'image': img_relative
        }
    )
    if created:
        print(f"Added new product: {prod.name}")

print(f"Total Products in DB now: {Product.objects.count()}")
