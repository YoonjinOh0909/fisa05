import json
from pathlib import Path
from step_2_1 import OUT_DIR
from step_2_2 import get_total_filesize
from step_2_3 import load_dirnames

OUT_2_4 = OUT_DIR / f"{Path(__file__).stem}.json"

def dump_filesize_from_dirnames():
    dirs = load_dirnames()
    result = {}
    for path_str in dirs:
        path = Path(path_str)
        filesize = get_total_filesize(path, pattern = "**/*")
        result[path.as_posix()] = filesize # as_posix() 저장된 Path 객체를 문자열로 반환
    with open(OUT_2_4, "w", encoding="utf-8") as fp:
        json.dump(result, fp, ensure_ascii=False, indent=2) # dump() -> json 형식의 문자열로 저장

def load_filesize_per_dir() -> dict[str, int]:
    if OUT_2_4.is_file():
        with open(OUT_2_4, encoding="utf-8") as fp:
            return json.load(fp)
    return {}

if __name__ == "__main__":
    dump_filesize_from_dirnames()