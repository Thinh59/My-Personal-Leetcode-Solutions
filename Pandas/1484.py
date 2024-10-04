import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    res = activities.groupby("sell_date")["product"].agg("nuinque", lambda x: ",".join(sorted(set(x))))
    res.columns = ["num_sold", "products"]
    return res.reset_index()