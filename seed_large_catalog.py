import os
import django
from django.utils.text import slugify
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from django.contrib.auth.models import User
from store.models import Category, Product

def run():
    print("Seeding 130+ products for 11-12 full pages of products...")

    # Ensure admin superuser exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@luxehaven.com', 'admin123')

    # Clear existing
    Product.objects.all().delete()
    Category.objects.all().delete()

    categories_data = [
        "Electronics & Gadgets", 
        "Designer Apparel", 
        "Fine Jewelry & Watches", 
        "Leather Goods", 
        "Artisanal Fragrance", 
        "Luxury Home",
        "Sports & Outdoors",
        "Books & Stationery"
    ]
    
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

    category_objects = {}
    for cat_name in categories_data:
        cat = Category.objects.create(
            name=cat_name, 
            slug=slugify(cat_name),
            description=f"Explore our exclusive collection of {cat_name}."
        )
        category_objects[cat_name] = cat

    # Base list of 132 diverse luxury products
    base_products = [
        # Electronics & Gadgets (18)
        ("Wireless Noise-Canceling Headphones Pro", 299.99, 399.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?q=80&w=800&auto=format&fit=crop"),
        ("Smart Watch Titanium Edition", 449.99, 549.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=800&auto=format&fit=crop"),
        ("Hi-Fi Portable Bluetooth Speaker", 149.99, 199.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?q=80&w=800&auto=format&fit=crop"),
        ("Ultra-Slim Wireless Mechanical Keyboard", 129.99, 159.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1587829741301-dc798b83add3?q=80&w=800&auto=format&fit=crop"),
        ("Ergonomic Precision Wireless Mouse", 79.99, 99.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?q=80&w=800&auto=format&fit=crop"),
        ("Studio Monitoring In-Ear Monitors", 199.99, 249.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?q=80&w=800&auto=format&fit=crop"),
        ("4K Ultra HD Streaming Camera", 249.99, 299.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?q=80&w=800&auto=format&fit=crop"),
        ("MagSafe Dual Wireless Charging Stand", 89.99, 119.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1583863788434-e58a36330cf0?q=80&w=800&auto=format&fit=crop"),
        ("Portable Power Station 300W", 299.99, 349.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?q=80&w=800&auto=format&fit=crop"),
        ("Noise-Isolating Earbuds Active", 159.99, 189.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1572536147248-ac59a8abfa4b?q=80&w=800&auto=format&fit=crop"),
        ("Ultra HD Curved Monitor 34-Inch", 799.99, 899.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?q=80&w=800&auto=format&fit=crop"),
        ("Smart Home Temperature Hub", 119.99, 149.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1558002038-1055907df827?q=80&w=800&auto=format&fit=crop"),
        ("Smart LED Desk Lamp Touch", 69.99, 89.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1534073828943-f801091bb18c?q=80&w=800&auto=format&fit=crop"),
        ("Universal Fast Charge Hub 100W", 59.99, 79.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1585338107529-13afc5f02586?q=80&w=800&auto=format&fit=crop"),
        ("Virtual Reality Headset Pro", 499.99, 599.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1622979135225-d2ba269bc1bd?q=80&w=800&auto=format&fit=crop"),
        ("Wireless Audio Transmitter DAC", 179.99, 219.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1546435770-a3e426bf472b?q=80&w=800&auto=format&fit=crop"),
        ("Smart Fitness Ring Sensor", 249.99, 299.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1510017803434-a899398421b3?q=80&w=800&auto=format&fit=crop"),
        ("Compact Wireless Drone 4K", 649.99, 749.99, "Electronics & Gadgets", "https://images.unsplash.com/photo-1527977966376-1c8408f9f108?q=80&w=800&auto=format&fit=crop"),

        # Designer Apparel (18)
        ("Silk Cashmere Trench Overcoat", 1450.00, 1850.00, "Designer Apparel", "https://images.unsplash.com/photo-1539533018447-63fcce2678e3?q=80&w=800&auto=format&fit=crop"),
        ("Velvet Evening Tuxedo Jacket", 980.00, 1150.00, "Designer Apparel", "https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=800&auto=format&fit=crop"),
        ("Hand-Woven Merino Wool Blazer", 720.00, 890.00, "Designer Apparel", "https://images.unsplash.com/photo-1594938298603-c8148c4dae35?q=80&w=800&auto=format&fit=crop"),
        ("Pure Silk Plunge Evening Gown", 1650.00, 1950.00, "Designer Apparel", "https://images.unsplash.com/photo-1566174053879-31528523f8ae?q=80&w=800&auto=format&fit=crop"),
        ("Italian Cut Linen Summer Suit", 850.00, 990.00, "Designer Apparel", "https://images.unsplash.com/photo-1593032465175-481ac7f401a0?q=80&w=800&auto=format&fit=crop"),
        ("Classic Vintage Denim Jacket", 189.99, 249.99, "Designer Apparel", "https://images.unsplash.com/photo-1576995853123-5a10305d93c0?q=80&w=800&auto=format&fit=crop"),
        ("Organic Heavyweight Cotton Hoodie", 149.99, 189.99, "Designer Apparel", "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?q=80&w=800&auto=format&fit=crop"),
        ("Tailored Double-Breasted Trench", 890.00, 1050.00, "Designer Apparel", "https://images.unsplash.com/photo-1544441893-675973e31985?q=80&w=800&auto=format&fit=crop"),
        ("Pleated Silk Midi Skirt", 340.00, 420.00, "Designer Apparel", "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?q=80&w=800&auto=format&fit=crop"),
        ("Cashmere Crewneck Sweater", 380.00, 450.00, "Designer Apparel", "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?q=80&w=800&auto=format&fit=crop"),
        ("Satin Button-Down Silk Shirt", 260.00, 310.00, "Designer Apparel", "https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?q=80&w=800&auto=format&fit=crop"),
        ("Leather Moto Jacket Black", 1100.00, 1350.00, "Designer Apparel", "https://images.unsplash.com/photo-1551028719-00167b16eac5?q=80&w=800&auto=format&fit=crop"),
        ("Structured Tweed Tailored Vest", 290.00, 350.00, "Designer Apparel", "https://images.unsplash.com/photo-1509631179647-0177331693ae?q=80&w=800&auto=format&fit=crop"),
        ("Wool Blend Winter Overcoat", 650.00, 780.00, "Designer Apparel", "https://images.unsplash.com/photo-1539533018447-63fcce2678e3?q=80&w=800&auto=format&fit=crop"),
        ("Casual Oxford Cotton Shirt", 129.99, 159.99, "Designer Apparel", "https://images.unsplash.com/photo-1598033129183-c4f50c736f10?q=80&w=800&auto=format&fit=crop"),
        ("Ribbed Knit Alpaca Cardigan", 420.00, 490.00, "Designer Apparel", "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?q=80&w=800&auto=format&fit=crop"),
        ("Designer Tailored Trousers", 320.00, 390.00, "Designer Apparel", "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?q=80&w=800&auto=format&fit=crop"),
        ("Embroidered Velvet Slippers", 280.00, 340.00, "Designer Apparel", "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?q=80&w=800&auto=format&fit=crop"),

        # Fine Jewelry & Watches (18)
        ("Chronograph Tourbillon Platinum Edition", 4850.00, 5800.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1524805444758-089113d48a6d?q=80&w=800&auto=format&fit=crop"),
        ("Royal Oak Perpetual Calendar Rose Gold", 8200.00, 9500.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1523275335684-37898b6baf30?q=80&w=800&auto=format&fit=crop"),
        ("Submariner Automatic Diver Spec-1", 3200.00, 3800.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1539185441755-769473a23570?q=80&w=800&auto=format&fit=crop"),
        ("Vintage Skeleton GMT Automatic", 2950.00, 3400.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1509042239860-f550ce710b93?q=80&w=800&auto=format&fit=crop"),
        ("Solitaire Diamond Pendant 18k Gold", 2400.00, 2900.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?q=80&w=800&auto=format&fit=crop"),
        ("Emerald & Diamond Halo Ring", 3100.00, 3650.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1605100804763-247f67b3557e?q=80&w=800&auto=format&fit=crop"),
        ("South Sea Pearl & Diamond Earrings", 1850.00, 2200.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?q=80&w=800&auto=format&fit=crop"),
        ("Sapphire & Platinum Tennis Bracelet", 3900.00, 4500.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?q=80&w=800&auto=format&fit=crop"),
        ("18k Rose Gold Band Ring Minimalist", 650.00, 790.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1603561591411-07134e71a2a9?q=80&w=800&auto=format&fit=crop"),
        ("Diamond Pave Hoop Earrings 14k", 1250.00, 1450.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1630019852942-f89202989a59?q=80&w=800&auto=format&fit=crop"),
        ("Vintage Mechanical Moonphase Watch", 2800.00, 3200.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?q=80&w=800&auto=format&fit=crop"),
        ("Tahitian Black Pearl Pendant", 1450.00, 1750.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?q=80&w=800&auto=format&fit=crop"),
        ("Ruby & Diamond Statement Ring", 2900.00, 3400.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1605100804763-247f67b3557e?q=80&w=800&auto=format&fit=crop"),
        ("White Gold Bangle Diamond Inset", 2100.00, 2500.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1611591475281-b1c9c8141444?q=80&w=800&auto=format&fit=crop"),
        ("Automatic Skeleton Stainless Diver", 1950.00, 2300.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1524805444758-089113d48a6d?q=80&w=800&auto=format&fit=crop"),
        ("Signet Ring 18k Yellow Gold", 890.00, 1050.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1603561591411-07134e71a2a9?q=80&w=800&auto=format&fit=crop"),
        ("Choker Necklace Freshwater Pearls", 980.00, 1200.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?q=80&w=800&auto=format&fit=crop"),
        ("Diamond Stud Earrings 2-Carat", 3500.00, 4200.00, "Fine Jewelry & Watches", "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?q=80&w=800&auto=format&fit=crop"),

        # Leather Goods (16)
        ("Full-Grain Italian Calfskin Tote", 1250.00, 1500.00, "Leather Goods", "https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=800&auto=format&fit=crop"),
        ("Structured Crossbody Bag Gold Hardware", 890.00, 1050.00, "Leather Goods", "https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?q=80&w=800&auto=format&fit=crop"),
        ("Monogrammed All-Travel Duffle", 1100.00, 1350.00, "Leather Goods", "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?q=80&w=800&auto=format&fit=crop"),
        ("Minimalist Leather Zip Wallet", 195.00, 240.00, "Leather Goods", "https://images.unsplash.com/photo-1627123424574-724758594e93?q=80&w=800&auto=format&fit=crop"),
        ("Hand-Burnished Calfskin Belt", 145.00, 180.00, "Leather Goods", "https://images.unsplash.com/photo-1624222247344-550fb60583dc?q=80&w=800&auto=format&fit=crop"),
        ("Quilted Leather Chain Shoulder Bag", 950.00, 1150.00, "Leather Goods", "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?q=80&w=800&auto=format&fit=crop"),
        ("Executive Leather Briefcase Tan", 850.00, 990.00, "Leather Goods", "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?q=80&w=800&auto=format&fit=crop"),
        ("Compact Cardholder Grained Leather", 120.00, 150.00, "Leather Goods", "https://images.unsplash.com/photo-1627123424574-724758594e93?q=80&w=800&auto=format&fit=crop"),
        ("Saddle Shoulder Bag Brass Buckle", 680.00, 790.00, "Leather Goods", "https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?q=80&w=800&auto=format&fit=crop"),
        ("Leather Passport Folio Case", 160.00, 195.00, "Leather Goods", "https://images.unsplash.com/photo-1627123424574-724758594e93?q=80&w=800&auto=format&fit=crop"),
        ("Suede Bucket Bag Chestnut", 590.00, 690.00, "Leather Goods", "https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=800&auto=format&fit=crop"),
        ("Travel Toiletry Kit Full-Grain", 220.00, 260.00, "Leather Goods", "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?q=80&w=800&auto=format&fit=crop"),
        ("Woven Leather Tote Bag Natural", 780.00, 920.00, "Leather Goods", "https://images.unsplash.com/photo-1584917865442-de89df76afd3?q=80&w=800&auto=format&fit=crop"),
        ("Classic Reversible Leather Belt", 165.00, 195.00, "Leather Goods", "https://images.unsplash.com/photo-1624222247344-550fb60583dc?q=80&w=800&auto=format&fit=crop"),
        ("Slim Leather Laptop Sleeve 15-Inch", 210.00, 250.00, "Leather Goods", "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?q=80&w=800&auto=format&fit=crop"),
        ("Structured Top-Handle Satchel", 890.00, 1050.00, "Leather Goods", "https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?q=80&w=800&auto=format&fit=crop"),

        # Artisanal Fragrance (14)
        ("Oud & Royal Rose Extrait 100ml", 380.00, 450.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1541643600914-78b084683601?q=80&w=800&auto=format&fit=crop"),
        ("Velvet Amber & Vanilla Absolute 50ml", 290.00, 340.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?q=80&w=800&auto=format&fit=crop"),
        ("Citrus Bergamot & Vetiver Eau de Parfum", 240.00, 280.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1594035910387-fea47794261f?q=80&w=800&auto=format&fit=crop"),
        ("Smoked Cedar & Santal Cologne", 260.00, 310.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1541643600914-78b084683601?q=80&w=800&auto=format&fit=crop"),
        ("Jasmin Nocturne Perfume Extract", 350.00, 420.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?q=80&w=800&auto=format&fit=crop"),
        ("Wild Fig & Neroli Room Spray", 85.00, 105.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1594035910387-fea47794261f?q=80&w=800&auto=format&fit=crop"),
        ("Artisanal Scented Soy Candle Oud", 95.00, 120.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?q=80&w=800&auto=format&fit=crop"),
        ("Iris & Tobacco Leaf Eau de Parfum", 280.00, 330.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1541643600914-78b084683601?q=80&w=800&auto=format&fit=crop"),
        ("Black Sea Salt & Driftwood Perfume", 220.00, 260.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1594035910387-fea47794261f?q=80&w=800&auto=format&fit=crop"),
        ("White Musk & Cashmere Mist", 185.00, 220.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?q=80&w=800&auto=format&fit=crop"),
        ("Botanical Hair Fragrance Oil", 95.00, 120.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1535585209827-a15fcdbc4c2d?q=80&w=800&auto=format&fit=crop"),
        ("Rosewood & Cardamom Solid Perfume", 110.00, 135.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1541643600914-78b084683601?q=80&w=800&auto=format&fit=crop"),
        ("Luxurious Body Elixir Patchouli", 140.00, 170.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?q=80&w=800&auto=format&fit=crop"),
        ("Discovery Fragrance Set 5x10ml", 160.00, 195.00, "Artisanal Fragrance", "https://images.unsplash.com/photo-1594035910387-fea47794261f?q=80&w=800&auto=format&fit=crop"),

        # Luxury Home (16)
        ("Hand-Blown Crystal Decanter Set", 520.00, 650.00, "Luxury Home", "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?q=80&w=800&auto=format&fit=crop"),
        ("Egyptian Cotton 1000TC Sheet Set", 420.00, 490.00, "Luxury Home", "https://images.unsplash.com/photo-1631679706909-1844bbd07221?q=80&w=800&auto=format&fit=crop"),
        ("Marble & Brass Table Lamp", 380.00, 450.00, "Luxury Home", "https://images.unsplash.com/photo-1534073828943-f801091bb18c?q=80&w=800&auto=format&fit=crop"),
        ("Hand-Woven Cashmere Throw Blanket", 490.00, 580.00, "Luxury Home", "https://images.unsplash.com/photo-1584100936595-c0654b55a2e2?q=80&w=800&auto=format&fit=crop"),
        ("Artisan Ceramic Dinnerware Set", 340.00, 420.00, "Luxury Home", "https://images.unsplash.com/photo-1584992236310-6edddc08acff?q=80&w=800&auto=format&fit=crop"),
        ("Velvet Accent Lounge Chair", 890.00, 1050.00, "Luxury Home", "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?q=80&w=800&auto=format&fit=crop"),
        ("Handcrafted Brass Wall Mirror", 290.00, 360.00, "Luxury Home", "https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?q=80&w=800&auto=format&fit=crop"),
        ("Aromatherapy Diffuser Glass Dome", 135.00, 165.00, "Luxury Home", "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?q=80&w=800&auto=format&fit=crop"),
        ("Bamboo Organic Fiber Duvet Cover", 280.00, 340.00, "Luxury Home", "https://images.unsplash.com/photo-1631679706909-1844bbd07221?q=80&w=800&auto=format&fit=crop"),
        ("Minimalist Solid Oak Side Table", 450.00, 540.00, "Luxury Home", "https://images.unsplash.com/photo-1532323544230-7191fd51bc1b?q=80&w=800&auto=format&fit=crop"),
        ("Stained Glass Table Vase Gold Rim", 175.00, 210.00, "Luxury Home", "https://images.unsplash.com/photo-1578500494198-246f612d3b3d?q=80&w=800&auto=format&fit=crop"),
        ("Hand-Tufted Wool Area Rug", 750.00, 890.00, "Luxury Home", "https://images.unsplash.com/photo-1600121848594-d8644e57abab?q=80&w=800&auto=format&fit=crop"),
        ("Luxury Linen Napkin Set 6pc", 95.00, 120.00, "Luxury Home", "https://images.unsplash.com/photo-1584992236310-6edddc08acff?q=80&w=800&auto=format&fit=crop"),
        ("Teak Wood Cheese Serving Board", 110.00, 140.00, "Luxury Home", "https://images.unsplash.com/photo-1590794056226-77ef3a6c474e?q=80&w=800&auto=format&fit=crop"),
        ("Brass Candleholder Set 3-Piece", 160.00, 195.00, "Luxury Home", "https://images.unsplash.com/photo-1608571423902-eed4a5ad8108?q=80&w=800&auto=format&fit=crop"),
        ("Crystal Cocktail Glassware Set", 240.00, 290.00, "Luxury Home", "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?q=80&w=800&auto=format&fit=crop"),

        # Sports & Outdoors (12)
        ("Pro Non-Slip Natural Rubber Yoga Mat", 120.00, 150.00, "Sports & Outdoors", "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?q=80&w=800&auto=format&fit=crop"),
        ("Heavyweight Latex Resistance Band Set", 49.99, 69.99, "Sports & Outdoors", "https://images.unsplash.com/photo-1598289431512-b97b0917affc?q=80&w=800&auto=format&fit=crop"),
        ("Ergonomic Waterproof Backpack 45L", 189.99, 239.99, "Sports & Outdoors", "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?q=80&w=800&auto=format&fit=crop"),
        ("Speed Cable Weighted Jump Rope", 34.99, 49.99, "Sports & Outdoors", "https://images.unsplash.com/photo-1599058945522-28d584b6f0ff?q=80&w=800&auto=format&fit=crop"),
        ("Stainless Thermal Hydration Flask", 45.00, 59.99, "Sports & Outdoors", "https://images.unsplash.com/photo-1602143407151-7111542de6e8?q=80&w=800&auto=format&fit=crop"),
        ("Pro Fitness Recovery Foam Roller", 55.00, 75.00, "Sports & Outdoors", "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?q=80&w=800&auto=format&fit=crop"),
        ("Lightweight Trail Running Shoes", 169.99, 199.99, "Sports & Outdoors", "https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=800&auto=format&fit=crop"),
        ("Adjustable Steel Dumbbell Pair", 299.99, 360.00, "Sports & Outdoors", "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?q=80&w=800&auto=format&fit=crop"),
        ("High-Density Fitness Exercise Mat", 85.00, 110.00, "Sports & Outdoors", "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?q=80&w=800&auto=format&fit=crop"),
        ("Polarized Performance Sport Sunglasses", 149.99, 189.99, "Sports & Outdoors", "https://images.unsplash.com/photo-1511499767150-a48a237f0083?q=80&w=800&auto=format&fit=crop"),
        ("Ultra-Lightweight Camping Tent 2P", 349.99, 420.00, "Sports & Outdoors", "https://images.unsplash.com/photo-1504280390367-361c6d9f38f4?q=80&w=800&auto=format&fit=crop"),
        ("Thermal Down Sleeping Bag -10C", 249.99, 299.99, "Sports & Outdoors", "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?q=80&w=800&auto=format&fit=crop"),

        # Books & Stationery (14)
        ("The Art of Software Architecture", 59.99, 74.99, "Books & Stationery", "https://images.unsplash.com/photo-1532012197267-da84d127e765?q=80&w=800&auto=format&fit=crop"),
        ("Mindful Leadership & Executive Focus", 34.99, 44.99, "Books & Stationery", "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?q=80&w=800&auto=format&fit=crop"),
        ("Modern Digital Brand Strategy", 42.99, 54.99, "Books & Stationery", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800&auto=format&fit=crop"),
        ("Creative Writing & Storytelling Masterclass", 29.99, 39.99, "Books & Stationery", "https://images.unsplash.com/photo-1455390582262-044cdead277a?q=80&w=800&auto=format&fit=crop"),
        ("Full-Grain Leather Bound Journal", 65.00, 85.00, "Books & Stationery", "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?q=80&w=800&auto=format&fit=crop"),
        ("Fountain Pen Brass Gold Nib", 145.00, 180.00, "Books & Stationery", "https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?q=80&w=800&auto=format&fit=crop"),
        ("Minimalist Hardcover Weekly Planner", 38.00, 48.00, "Books & Stationery", "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?q=80&w=800&auto=format&fit=crop"),
        ("Collector Edition World History Atlas", 120.00, 150.00, "Books & Stationery", "https://images.unsplash.com/photo-1532012197267-da84d127e765?q=80&w=800&auto=format&fit=crop"),
        ("Design Systems & Visual Identity Book", 55.00, 69.99, "Books & Stationery", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800&auto=format&fit=crop"),
        ("Handmade Cotton Paper Notebook Set", 45.00, 58.00, "Books & Stationery", "https://images.unsplash.com/photo-1455390582262-044cdead277a?q=80&w=800&auto=format&fit=crop"),
        ("Calligraphy Pen & Ink Set Luxury Box", 110.00, 135.00, "Books & Stationery", "https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?q=80&w=800&auto=format&fit=crop"),
        ("Philosophy of Aesthetics Hardcover", 48.00, 60.00, "Books & Stationery", "https://images.unsplash.com/photo-1532012197267-da84d127e765?q=80&w=800&auto=format&fit=crop"),
        ("Italian Leather Bookmark Set 3pc", 35.00, 45.00, "Books & Stationery", "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?q=80&w=800&auto=format&fit=crop"),
        ("Archival Quality Fountain Pen Ink 50ml", 42.00, 55.00, "Books & Stationery", "https://images.unsplash.com/photo-1583485088034-697b5bc54ccd?q=80&w=800&auto=format&fit=crop"),
    ]

    count = 0
    for name, price, compare_price, cat_name, img_url in base_products:
        cat = category_objects[cat_name]
        is_featured = (count % 8 == 0)
        prod = Product.objects.create(
            name=name,
            slug=slugify(f"{name}-{count+1}"),
            description=f"Exquisite handcrafted {name}. Designed with meticulous attention to detail, premium materials, and unparalleled craftsmanship.",
            price=price,
            compare_price=compare_price,
            stock=random.randint(15, 60),
            category=cat,
            is_featured=is_featured,
            is_active=True
        )
        count += 1

    print(f"Successfully created {count} products! Generated 11 pages of products.")

if __name__ == '__main__':
    run()
