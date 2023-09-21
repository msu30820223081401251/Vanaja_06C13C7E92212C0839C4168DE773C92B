# linear_search_product
def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices
  product_list = ["apple", "banana", "apple", "orange"]
target_product = "apple"

result = linear_search_product(product_list, target_product)
print(result) 