from pathlib import Path
import pandas as pd
from step_1 import IN_DIR, OUT_DIR

OUT_2_2 = OUT_DIR / f"{Path(__file__).stem}.xlsx"

if __name__ == "__main__":
    result = []

    for xlsx_path in Path(IN_DIR).glob("2024년*월.xlsx"): # 정규식을 사용하기 위한 glob
        df_raw = pd.read_excel(xlsx_path, sheet_name="Sheet1", usecols="B:E", skiprows=2)

        result.append(df_raw)

    # result # result 에는 data frame 3가지가 있을 것이다.
    df_concat = pd.concat(result)
    df_concat.to_excel(OUT_2_2, index=False)
    # 이렇게 하면, 3개로 나눠진 파일들을 하나의 파일로 모을 수 있다.