import json
from pathlib import Path
from step_2_1 import OUT_DIR 
# 측정할 폴더 목록 저장하기

OUT_2_3 = OUT_DIR / f"{Path(__file__).stem}.json" # 파일 이름에서 확장자를 뺀 부분.

def dump_dirnames(base_dir : Path) -> None :
    dirs = []
    for path in base_dir.iterdir(): # iterdir() 주어진 폴더의 모든 파일과 하위 폴더 목록을 반환
        if path.is_dir():
            dirs.append(path.as_posix()) # as_posix는 저장된 Path 객체를 문자열로 반환
    dirs_sorted = sorted(dirs)
    with open(OUT_2_3, "w", encoding="utf-8") as fp:
        json.dump(dirs_sorted, fp, ensure_ascii=False, indent=2)

def load_dirnames() -> list[str]:
    if OUT_2_3.is_file():
        with open(OUT_2_3, encoding="utf-8") as fp:
            return json.load(fp)
    return []

if __name__ == "__main__":
    dump_dirnames(Path.home())