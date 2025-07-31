import pandas as pd

def delta_buss_days(date1, date2):
    d1 = pd.to_datetime(date1)
    d2 = pd.to_datetime(date2)
    ans = pd.bdate_range(d1, d2)
    return len(ans)
