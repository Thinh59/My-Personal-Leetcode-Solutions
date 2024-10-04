import pandas as pd
import numpy as np

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    first_merge = students.merge(subjects, how='cross')
    examinations['attended_exams'] = 1

    merged = first_merge.merge(examinations, on =['student_id', 'subject_name'], how='outer').fillna(0)

    grouped = merged.groupby(by=['student_id', 'student_name', 'subject_name'])['attended_exams'].sum().reset_index()
    grouped.loc[grouped['student_name']==0, 'student_name'] = np.nan
    return grouped