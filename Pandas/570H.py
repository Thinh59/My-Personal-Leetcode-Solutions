import pandas as pd

data = [
    {"id": 101, "name": "John", "department": "A", "managerId": None},
    {"id": 102, "name": "Dan", "department": "A", "managerId": 101},
    {"id": 103, "name": "James", "department": "A", "managerId": 101},
    {"id": 104, "name": "Amy", "department": "A", "managerId": 101},
    {"id": 105, "name": "Anne", "department": "A", "managerId": 101},
    {"id": 106, "name": "Ron", "department": "B", "managerId": 101}
]
employee = pd.DataFrame(data)

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    direct_reports_count = employee.groupby('managerId')['id'].count().reset_index(name='report_count')
    managers_with_five_reports = direct_reports_count[direct_reports_count['report_count'] >= 5]
    manager = pd.merge(managers_with_five_reports, employee, left_on='managerId', right_on='id', how='inner')
    print(manager)

    return manager[['name']]

print(find_managers(employee))