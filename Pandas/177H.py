import pandas as pd

employee = pd.DataFrame({"id" : [1, 2, 3], "salary" : [100, 200, 300]})
n = 3
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted = employee["salary"].sort_values(ascending = False).drop_duplicates()
    #Không thể thay sortd = employee["Rank"] vì khi drop_duplicates sẽ gây ra tình trạng thiếu dòng và không khớp với DataFrame

    if N < 1 or N > len(sorted):
        return pd.DataFrame({f"getNthHighestSalary({N})" : [None]})
    
    res = sorted.iloc[N - 1]

    return pd.DataFrame({f"getNthHighestSalary({N})" : [res]})

print(nth_highest_salary(employee, n))