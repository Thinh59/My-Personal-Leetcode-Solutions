import pandas as pd

employees = pd.DataFrame({"emp_id" : [1, 1, 1, 2, 2], "event_day" : ["2020-11-28", "2020-11-28", "2020-12-03", "2020-11-28", "2020-12-09"], "in_time" : [4, 55, 1, 3, 47], "out_time" : [32, 200, 42, 33, 74]})

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    res = employees.groupby(by = ["event_day", "emp_id"])[["out_time", "in_time"]].sum().reset_index()
    res["total_time"] = res["out_time"] - res["in_time"]
    res = res.rename(columns = {"event_day" : "day"})
    return res[["day", "emp_id", "total_time"]]
print(total_time(employees))