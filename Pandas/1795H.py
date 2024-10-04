import pandas as pd

products = pd.DataFrame({"product_id" : [0, 1], "store1": [95, 70], "store2" : [100, None], "store3": [105, 80]})

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    modified_table = products.set_index('product_id').stack().reset_index()
    modified_table.columns = ["product_id", "store", "price"]
    return modified_table

print(rearrange_products_table(products))