import os
import shutil
from pathlib import Path

# 다운로드 폴더 경로
download_folder = r"C:\Users\Oh\Downloads"

# 파일 분류 설정
file_categories = {
    r"\images": ["*.jpg", "*.jpeg"],
    r"\data": ["*.csv", "*.xlsx"],
    r"\docs": ["*.txt", "*.doc", "*.pdf"],
    r"\archive": ["*.zip"]
}

# 다운로드 폴더가 존재하는지 확인
if not os.path.exists(download_folder):
    print(f"오류: {download_folder} 폴더를 찾을 수 없습니다.")
    exit()

# 대상 폴더 생성 및 파일 이동
for folder_suffix, extensions in file_categories.items():
    target_folder = download_folder + folder_suffix
    
    # 폴더가 없으면 생성
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        print(f"✓ 폴더 생성: {target_folder}")
    
    # 각 확장자별로 파일 이동
    for ext in extensions:
        # 다운로드 폴더에서 해당 확장자 파일 찾기
        for file in Path(download_folder).glob(ext):
            if file.is_file():
                source_path = file
                dest_path = os.path.join(target_folder, file.name)
                
                try:
                    shutil.move(str(source_path), dest_path)
                    print(f"✓ 이동: {file.name} → {target_folder}")
                except Exception as e:
                    print(f"✗ 오류: {file.name} 이동 실패 - {e}")

print("\n=== 파일 정렬 완료 ===")