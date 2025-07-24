from pathlib import Path
import matplotlib.pyplot as plt
from step_2_1 import OUT_DIR
from step_3_1 import load_plot_data

plot_data = load_plot_data()

# fig 는 차트의 배경
# axes 는 차트를 실제로 생성하고, 제목 축 등 세부 설정 처리.
fig, ax = plt.subplots()

# ax.barh(세로축에 입력될 값, 가로축에 입력될 값)
ax.barh(plot_data["stem"], plot_data["size"])


fig.savefig(OUT_DIR/ f"{Path(__file__).stem}.png")