from PIL import Image
import os
import shutil

def is_color_image(image_path):
    img = Image.open(image_path)
    rgb_values = img.getcolors(maxcolors=255*255*255)
    if rgb_values is None:
        return False  # 如果无法获取RGB值，则认为不是彩色图像
    return len(rgb_values) > 1024  # 通常彩色图像的RGB值种类较多

def move_color_images(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # 遍历源文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                source_path = os.path.join(root, filename)
                if is_color_image(source_path):
                    destination_path = os.path.join(destination_folder, filename)
                    shutil.move(source_path, destination_path)
                    print(f"Moved {filename} to {destination_folder}")


# 指定源文件夹和目标文件夹路径
source_folder ="outputs2"
destination_folder = "out"

# 调用函数移动彩色图像
move_color_images(source_folder, destination_folder)
