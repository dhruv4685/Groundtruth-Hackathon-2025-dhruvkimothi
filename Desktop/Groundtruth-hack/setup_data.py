import pandas as pd
import json
import random

def generate_enterprise_data():
    print("🚀 Generating Global-Scale Mock Data...")

    
    categories = ["Beverage", "Apparel", "Electronics", "Snacks", "Home", "Footwear"]
    locations = ["Aisle 1", "Aisle 2", "Aisle 3", "Aisle 4", "Counter", "Checkout Zone", "Frozen Section"]
    offers = ["None", "Buy 1 Get 1", "10% Off", "20% Off", "Clearance", "Member Exclusive"]
    stock_levels = ["In Stock", "In Stock", "In Stock", "Low Stock (2 left)", "Out of Stock"] 
    
    
    fixed_items = [
        {"Product": "Hot Cocoa", "Category": "Beverage", "Price": 4.50, "Stock": "In Stock", "Location": "Counter", "Weather_Tag": "Cold", "Offer": "10% Off (Code: COCOA10)"},
        {"Product": "Premium Umbrella", "Category": "Apparel", "Price": 25.00, "Stock": "Out of Stock", "Location": "Aisle 1", "Weather_Tag": "Rain", "Offer": "None"},
        {"Product": "Winter Down Jacket", "Category": "Apparel", "Price": 150.00, "Stock": "Low Stock (1 left)", "Location": "Aisle 3", "Weather_Tag": "Cold", "Offer": "Clearance"},
        {"Product": "Iced Lemonade", "Category": "Beverage", "Price": 3.00, "Stock": "In Stock", "Location": "Counter", "Weather_Tag": "Hot", "Offer": "None"},
        {"Product": "Rain Boots", "Category": "Footwear", "Price": 45.00, "Stock": "In Stock", "Location": "Aisle 2", "Weather_Tag": "Rain", "Offer": "15% Off"}
    ]
    generated_items = []
    adjectives = ["Organic", "Premium", "Budget", "Classic", "Spicy", "Vanilla", "Travel", "Smart"]
    nouns = ["Coffee", "Tea", "Chips", "Charger", "Towel", "Scarf", "Water Bottle", "Headphones"]
    
    for i in range(100):
        adj = random.choice(adjectives)
        noun = random.choice(nouns)
        item = {
            "Product": f"{adj} {noun}",
            "Category": random.choice(categories),
            "Price": round(random.uniform(2.00, 200.00), 2),
            "Stock": random.choice(stock_levels),
            "Location": random.choice(locations),
            "Weather_Tag": "Neutral", 
            "Offer": random.choice(offers)
        }
        generated_items.append(item)

    full_inventory = fixed_items + generated_items
    
   
    df = pd.DataFrame(full_inventory)
    df.to_csv("store_inventory.csv", index=False)
    print(f"✅ Created 'store_inventory.csv' with {len(full_inventory)} items.")

    #CREATE USER PROFILE (JSON) ---
    # We create ONE specific user ("Dhruv") to ensure the demo is safe/consistent.
    users = {
        "user_dhruv": {
            "name": "Dhruv",
            "tier": "Gold Member",
            "preferences": ["Hates Rain", "Loves Coffee", "Tech Enthusiast"],
            "last_visit": "2 days ago",
            "points": 1450
        }
    }
    
    with open("user_profile.json", "w") as f:
        json.dump(users, f, indent=4)
    print("✅ Created 'user_profile.json' for user: Dhruv")

if __name__ == "__main__":
    generate_enterprise_data()