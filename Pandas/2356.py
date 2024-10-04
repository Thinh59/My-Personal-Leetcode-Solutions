import pandas as pd

teacher = pd.DataFrame({"teacher_id" : [1, 1, 1, 2, 2, 2, 2], "subject_id" : [2, 2, 3, 1, 2, 3, 4], "dept_id" : [3, 4, 3, 1, 1, 1, 1]})
def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby("teacher_id")["subject_id"].nunique().reset_index(name = "count")
print(count_unique_subjects(teacher))