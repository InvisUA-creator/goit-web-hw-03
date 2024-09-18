import os
import sys
import shutil
from concurrent.futures import ThreadPoolExecutor


def copy_file_to_target(file_path, target_dir):
    file_extension = os.path.splitext(file_path)[1][1:].lower()
    if file_extension:
        target_folder = os.path.join(target_dir, file_extension)
        os.makedirs(target_folder, exist_ok=True)

        shutil.copy(file_path, target_folder)
        print(f"Копіюємо {file_path} до {target_folder}")


def process_directory(source_dir, target_dir, file_copy_executor):
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_copy_executor.submit(copy_file_to_target, file_path, target_dir)


def main():
    if len(sys.argv) < 2:
        print("Вкажіть шлях до джерельної директорії для обробки.")
        return

    source_dir = sys.argv[1]
    target_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    if not os.path.exists(source_dir):
        print(f"Директорія {source_dir} не існує.")
        return

    os.makedirs(target_dir, exist_ok=True)

    with ThreadPoolExecutor() as file_copy_executor:
        process_directory(source_dir, target_dir, file_copy_executor)


if __name__ == "__main__":
    main()
