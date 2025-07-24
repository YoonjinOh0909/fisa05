import pandas as pd
from step_1 import IN_DIR

df_raw = pd.read_excel((IN_DIR / "2024년1월.xlsx"),
                        sheet_name = "Sheet1", usecols = "B:E", skiprows =2)
                    # sheet_name 지정, col, row의 옵션을 선택할 수 있다.

df_raw