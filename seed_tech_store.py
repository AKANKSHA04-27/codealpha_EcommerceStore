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
categories_dir = os.path.join(media_dir, 'categories')

os.makedirs(products_dir, exist_ok=True)
os.makedirs(categories_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def download_image(url, filepath):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        print(f"Downloaded: {os.path.basename(filepath)}")
        return True
    except Exception as e:
        print(f"Failed download: {e}")
        return False

# Clear old entries for fresh tech rebranding
Product.objects.all().delete()
Category.objects.all().delete()

tech_categories = [
    {"name": "Quantum Hardware", "url": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?q=80&w=800&auto=format&fit=crop"},
    {"name": "Neural Accelerators", "url": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=800&auto=format&fit=crop"},
    {"name": "Enterprise Cloud Racks", "url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=800&auto=format&fit=crop"},
    {"name": "Cybernetic Workstations", "url": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=800&auto=format&fit=crop"},
    {"name": "Autonomous Edge Modules", "url": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=800&auto=format&fit=crop"},
    {"name": "Developer Software Kits", "url": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=800&auto=format&fit=crop"}
]

cat_objs = {}
for c in tech_categories:
    slug = slugify(c["name"])
    fn = f"{slug}.jpg"
    fp = os.path.join(categories_dir, fn)
    img_rel = ""
    if download_image(c["url"], fp):
        img_rel = f"categories/{fn}"
    cat = Category.objects.create(name=c["name"], slug=slug, image=img_rel)
    cat_objs[c["name"]] = cat

tech_products = [
    # Quantum Hardware
    {"name": "Nexus Q-Core 128 Qubit Processor", "price": 14999.00, "compare_price": 17999.00, "category": "Quantum Hardware", "is_featured": True, "desc": "Sub-Kelvin cryogenic quantum processing unit designed for ultra-low decoherence machine learning models.", "url": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?q=80&w=800&auto=format&fit=crop"},
    {"name": "Aura Cryo-Chamber Super Module", "price": 28999.00, "compare_price": 34000.00, "category": "Quantum Hardware", "is_featured": True, "desc": "Liquid helium isolation housing with zero-noise magnetic shielding for quantum computing nodes.", "url": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=800&auto=format&fit=crop"},
    {"name": "OptiWave Quantum Photonic Interconnect", "price": 8499.00, "compare_price": None, "category": "Quantum Hardware", "is_featured": False, "desc": "Terabit-per-second laser optical link for zero-latency inter-chip quantum state transfer.", "url": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?q=80&w=800&auto=format&fit=crop"},

    # Neural Accelerators
    {"name": "TensorNode H200 AI Compute Array", "price": 9999.00, "compare_price": 12499.00, "category": "Neural Accelerators", "is_featured": True, "desc": "Dual-die 141GB HBM3e AI accelerator delivering 4.8 PFLOPS of FP8 precision inference throughput.", "url": "https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?q=80&w=800&auto=format&fit=crop"},
    {"name": "Synapse-X Neuromorphic Chipset", "price": 4499.00, "compare_price": 5299.00, "category": "Neural Accelerators", "is_featured": True, "desc": "Spiking neural network processor modeling 10 million biological neurons with 1-watt power draw.", "url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=800&auto=format&fit=crop"},
    {"name": "HyperMatrix PFLOPS PCIe Acceleration Card", "price": 6299.00, "compare_price": None, "category": "Neural Accelerators", "is_featured": False, "desc": "Enterprise PCIe 5.0 expansion card tailored for trillion-parameter LLM fine-tuning pipelines.", "url": "https://images.unsplash.com/photo-1562976540-1502c2145186?q=80&w=800&auto=format&fit=crop"},

    # Enterprise Cloud Racks
    {"name": "Nexus Pod X-100 Hyperscale Rack", "price": 49999.00, "compare_price": 58000.00, "category": "Enterprise Cloud Racks", "is_featured": True, "desc": "Direct-to-chip liquid-cooled 42U rack engineered for private LLM training and sovereign cloud deployments.", "url": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?q=80&w=800&auto=format&fit=crop"},
    {"name": "Aethel-Fiber 800G Switch Chassis", "price": 12499.00, "compare_price": 14999.00, "category": "Enterprise Cloud Racks", "is_featured": False, "desc": "Ultra-low latency InfiniBand network switch with 64 ports of non-blocking 800Gb/s throughput.", "url": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?q=80&w=800&auto=format&fit=crop"},

    # Cybernetic Workstations
    {"name": "OmniStudio AI Founder Workstation", "price": 7999.00, "compare_price": 8999.00, "category": "Cybernetic Workstations", "is_featured": True, "desc": "Liquid-cooled desktop monster featuring quad RTX 4090 GPUs, 256GB ECC RAM, and dual Threadripper PRO.", "url": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=800&auto=format&fit=crop"},
    {"name": "CyberDeck Matrix Portable Dev Node", "price": 3499.00, "compare_price": None, "category": "Cybernetic Workstations", "is_featured": False, "desc": "Ruggedized portable AI inference terminal with integrated OLED telemetry HUD and 128GB unified memory.", "url": "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?q=80&w=800&auto=format&fit=crop"},

    # Autonomous Edge Modules
    {"name": "Aura Edge-AI Robotics Core", "price": 1899.00, "compare_price": 2299.00, "category": "Autonomous Edge Modules", "is_featured": True, "desc": "IP67 weather-sealed embedded Jetson Orin module for real-time computer vision and autonomous drones.", "url": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=800&auto=format&fit=crop"},
    {"name": "LidarSight 360 Spatial Sensor Array", "price": 2499.00, "compare_price": None, "category": "Autonomous Edge Modules", "is_featured": False, "desc": "Solid-state 3D LiDAR sensor mapping environments at 300 meters range with sub-centimeter accuracy.", "url": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?q=80&w=800&auto=format&fit=crop"},

    # Developer Software Kits
    {"name": "Nexus AI OS Enterprise License Key", "price": 999.00, "compare_price": 1499.00, "category": "Developer Software Kits", "is_featured": True, "desc": "Per-node enterprise software license with automated model sharding, zero-trust auth, and SLA guarantees.", "url": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?q=80&w=800&auto=format&fit=crop"},
    {"name": "QuantumSDK Developer Pro Pass", "price": 599.00, "compare_price": None, "category": "Developer Software Kits", "is_featured": False, "desc": "Full access to Python C++ quantum compiler, circuit simulators, and direct QPU execution credits.", "url": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?q=80&w=800&auto=format&fit=crop"}
]

for p in tech_products:
    cat = cat_objs[p["category"]]
    slug = slugify(p["name"])
    fn = f"{slug}.jpg"
    fp = os.path.join(products_dir, fn)
    img_rel = ""
    if download_image(p["url"], fp):
        img_rel = f"products/{fn}"
    
    prod = Product.objects.create(
        name=p["name"],
        slug=slug,
        description=p["desc"],
        price=p["price"],
        compare_price=p.get("compare_price"),
        stock=random.randint(15, 60),
        category=cat,
        is_featured=p["is_featured"],
        is_active=True,
        image=img_rel
    )
    print(f"Created tech product: {prod.name}")

print(f"Total Tech Products created: {Product.objects.count()}")
