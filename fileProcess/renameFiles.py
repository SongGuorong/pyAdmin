import os
import argparse

"""
@author: songguorong
@date: 2024-07-27
@desc: 将文件及其子文件名称前缀'_' 批量改成 '.'
"""


def rename_files(directory):
    # 遍历目标文件夹及其所有子文件夹中的所有文件
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.startswith('_'):
                # 构造旧文件名和新文件名的完整路径
                old_file = os.path.join(root, filename)
                new_file = os.path.join(root, '.' + filename[1:])
                # 重命名文件
                os.rename(old_file, new_file)
                print(f'Renamed: {old_file} -> {new_file}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename files in the specified directory and its subdirectories.")
    parser.add_argument("directory", help="The path to the directory containing files to be renamed.")
    args = parser.parse_args()

    rename_files(args.directory)
