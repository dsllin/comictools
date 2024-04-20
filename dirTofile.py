import os

def move_and_rename_images(source_folder, destination_folder):
    # 遍历源文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # 检查文件是否是图片文件（你可以根据需要扩展这个检查）
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                source_file_path = os.path.join(root, file)
                
                # 提取子文件夹名作为前缀
                prefix = os.path.basename(root)

                #使用utf-8编码，转换非英文字符方便图片处理
                # prefix = prefix.encode('unicode-escape').decode()
                # prefix = prefix.replace("\\", "")
                
                # 构建新的文件名
                new_file_name = f"{prefix}_{file}"
                
                # 构建目标文件路径
                destination_file_path = os.path.join(destination_folder, new_file_name)
                
                # 移动文件并重命名
                os.rename(source_file_path, destination_file_path)
                print(f"Moved {source_file_path} to {destination_file_path}")

# 指定源文件夹和目标文件夹
source_folder = 'inputs'
destination_folder = 'outputs'

# 调用函数来移动和重命名图片文件
move_and_rename_images(source_folder, destination_folder)
