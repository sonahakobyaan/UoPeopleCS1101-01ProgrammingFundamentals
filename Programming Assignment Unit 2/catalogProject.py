
# Part 2: Catalog Project

def generate_catalog():
    # Define base prices for the three items
    item1 = 200.0
    item2 = 400.0
    item3 = 600.0
    
    # Calculate discounted combos (10% discount)
    # Formula: (Price A + Price B) * 0.90
    combo1 = (item1 + item2) * 0.9
    combo2 = (item2 + item3) * 0.9
    combo3 = (item1 + item3) * 0.9
    
    # Calculate Gift Pack (Combo 4) with 25% discount
    # Formula: (Price A + Price B + Price C) * 0.75
    gift_pack = (item1 + item2 + item3) * 0.75
    
    # Display the catalog in the requested format
    print("Online Store")
    print("-" * 30)
    print(f"{'Product(S)':<25} {'Price'}")
    print(f"{'Item 1':<25} {item1}")
    print(f"{'Item 2':<25} {item2}")
    print(f"{'Item 3':<25} {item3}")
    print(f"{'Combo 1(Item 1 + 2)':<25} {combo1}")
    print(f"{'Combo 2(Item 2 + 3)':<25} {combo2}")
    print(f"{'Combo 3(Item 1 + 3)':<25} {combo3}")
    print(f"{'Combo 4(Item 1 + 2 + 3)':<25} {gift_pack}")
    print("-" * 30)
    print("For delivery Contact:98764678899")

# Execute the function to show output
generate_catalog()