# 작업 폴더 생성하기

from pathlib import Path # pathlib 패키지의 Path 클래스를 불러온다.

WORK_DIR = Path(__file__).parent # __file__ 은 현재 파일의 절대 경로
OUT_DIR = WORK_DIR / "output" # 나누기 표시가 아니라 경로에 '/'가 붙은거라서 추가 경로를 입력한 것과 같다.

if __name__ == "__main__": # 확장자를 제외한 현재 파일명.
    OUT_DIR.mkdir(exist_ok= True)