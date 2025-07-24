from pathlib import Path
import pandas as pd
from step_1 import OUT_DIR
from step_2_2 import OUT_2_2

OUT_3_2 = OUT_DIR / f"{Path(__file__).stem}.xlsx"

if __name__ == "__main__":
    df_raw = pd.read_excel(OUT_2_2)
    # df_raw.head()
    # 	거래일시	         가맹점명	분류	    사용금액
    # 0	2024-01-01 19:40	애플스토어	전자기기	69800
    # 1	2024-01-02 09:55	이디야 커피	카페/음료	6000
    # 2	2024-01-03 17:42	메가박스	영화	    11000
    # 3	2024-01-04 16:51	코레일	    대중교통	3000
    # 4	2024-01-06 14:50	유니클로	의류	    85000
    # df_pivot_1 = pd.pivot_table(df_raw, index = "분류", values="사용금액", aggfunc="sum")
    df_raw["거래연월"] = df_raw["거래일시"].str.slice(0,7)
    # df_raw

    df_pivot_2 = pd.pivot_table(df_raw, index="분류", columns="거래연월", values="사용금액", aggfunc="sum")
    df_pivot_2["누적금액"] = df_pivot_2.sum(axis=1)
    # df_pivot_2

    df_sort = df_pivot_2.sort_values("누적금액", ascending=False)
    # df_sort

    df_reindex = df_sort.reset_index()
    # df_reindex
    df_reindex.to_excel(OUT_3_2, index= False, sheet_name="분류별누적금액")