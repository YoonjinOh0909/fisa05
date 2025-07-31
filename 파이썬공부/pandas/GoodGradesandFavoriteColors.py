# https://www.interviewquery.com/questions/good-grades-and-favorite-colors

import pandas as pd

def grades_colors(students_df: pd.DataFrame):
    # return students_df[((students_df["favorite_color"] == 'green') | (students_df["favorite_color"] == 'red')) & (students_df.grade > 90)]
    return students_df[(students_df["favorite_color"].isin(['green', 'red']) ) & (students_df.grade > 90)]