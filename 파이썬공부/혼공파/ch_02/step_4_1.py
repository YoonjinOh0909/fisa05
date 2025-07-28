import pandas as pd
from step_3_2 import OUT_3_2

N = 4
df_raw = pd.read_excel(OUT_3_2)

df_head, df_tail = df_raw.iloc[:N], df_raw.iloc[N:]
# iloc를 통해서 행, 열을 원하는대로 빼낼 수 있다.
# a.iloc[:n, 0] n개의 행과 0번째 열을 반환한다.

df_tail
df_sum = df_tail.drop(columns=["분류"]).sum().to_frame().transpose()

# sum()을 하면 각 열에 있는 값들이 모두 합쳐진다. 이 때 분류 column에는 string 값들이 있지만 모두 합쳐진다.

df_sum["분류"] = "기타"
df_sum = df_sum.drop(labels="ss", axis=1)
df_sum

df_final = pd.concat([df_head, df_sum], ignore_index=True)
df_final

from pathlib import Path
import matplotlib.pyplot as plt
from step_1 import OUT_DIR

values = df_final["누적금액"]

fig, ax = plt.subplots(figsize = (16,9), dpi = 100)

ax.pie(
    values,
    textprops=dict(color="black", size = 20),
    startangle= 90,
    autopct="%.1f%%"
)
fig.savefig(OUT_DIR / f"{Path(__file__).stem}.png", bbox_inches='tight')