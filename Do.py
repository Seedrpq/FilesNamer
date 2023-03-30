import os
import re

# 定義要修改的資料夾所在的路徑
path = r'C:\Users\User\Downloads\Line\12345'

# 取得資料夾列表
folders = os.listdir(path)

# 定義增量
increment = 14

# 定義正則表達式來匹配符合要求的資料夾名稱
folder_regex = re.compile(r'^\d+_', re.IGNORECASE)

# 迭代每個資料夾
for folder in folders:
    print(f'處理資料夾：{folder}')
    # 如果資料夾名稱符合要求
    if folder_regex.match(folder):
        # 取得資料夾名稱中的數字部分
        num_str = re.search(r'^(\d+)_', folder).group(1)
        num = int(num_str)
        # 計算新的數字部分
        new_num = num + increment
        # 創建新名稱
        new_folder = folder.replace(num_str, str(new_num).zfill(len(num_str)))
        # 建立新資料夾路徑
        new_path = os.path.join(path, new_folder)
        # 重新命名資料夾
        os.rename(os.path.join(path, folder), new_path)
