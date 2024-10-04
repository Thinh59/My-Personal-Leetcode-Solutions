import pandas as pd
import numpy as np

ads = pd.DataFrame({"ad_id" : [1, 2, 3, 5, 1, 2, 3, 1, 2, 1], "user_id" : [1, 2, 3, 5, 7, 7, 5, 4, 11, 2], "action" : ["Clicked", "Clicked", "Viewed", "Ignored", "Ignored", "Viewed", "Clicked", "Viewed", "Viewed", "Clicked"]})
print(ads)
def ad_ctr(ads: pd.DataFrame) -> pd.DataFrame:
    res = ads.groupby(by = "ad_id")["action"].value_counts(normalize=True).unstack(fill_value= 0).reset_index()
    res["ctr"] = 0
    res["ctr"][res["Clicked"] + res["Viewed"] != 0] = res["Clicked"] / (res["Clicked"] + res["Viewed"]) * 100
    res["ad_id"] = np.arange(1, 5)
    res.rename(columns = {"action" : "ad_id"}, inplace=True)
    return res[["ad_id", "ctr"]]
print(ad_ctr(ads))