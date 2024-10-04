import pandas as pd

store = pd.DataFrame({"bill_id" : [6, 8, 4, 11, 13], "customer_id" : [1, 1, 2, 3, 3], "amount" : [549, 834, 394, 657, 257]})
def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    res = store["customer_id"][store["amount"] >= 500].drop_duplicates()
    return pd.DataFrame({"rich_count" : [len(res)]})

print(count_rich_customers(store))