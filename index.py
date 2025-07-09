# My Code
def sort_by_key(data, key):
    """
    Sort a list of dictionaries by a given key.
    """
    return sorted(data, key=lambda x: x[key])

# Example usage:
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 400}
]
# Copilot Code :
sorted_products = sort_by_key(products, "price")
print(sorted_products)

def sort_dictionaries_by_key(dictionaries, key):
    """
    Sort a list of dictionaries by a given key.
    """
    return sorted(dictionaries, key=lambda x: x[key])
