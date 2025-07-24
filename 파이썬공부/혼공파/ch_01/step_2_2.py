# 폴더 크기 측정 함수 만들기

from pathlib import Path
from step_2_1 import WORK_DIR # 이전에 작성한 모듈을 불러온다.

def get_total_filesize(base_dir: Path, pattern: str = "*") -> int:
    total_bytes = 0
    for fullpath in base_dir.glob(pattern): # 글로브 패턴과 일치하는 파일명을 리스트로 반환. *는 모든 파일을 뜻한다.
        if fullpath.is_file():
            total_bytes += fullpath.stat().st_size
    return total_bytes

if __name__ == "__main__": # 소스 코드 최초 실행시 실행. 다른 말로는 import 해서 사용할 때는 실행이 되지 않는다.
    base_dir = WORK_DIR
    filesize = get_total_filesize(base_dir, pattern="*")
    print(f"{base_dir.as_posix()=}, {filesize=} bytes")
