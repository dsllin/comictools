import os
import zipfile

def zip_subdirectories(root_directory,dtsdir):
    """
    给定一个目录，为其中的每个子目录创建独立的压缩文件
    """
    for subdir in os.listdir(root_directory):
        print(subdir)
        subdir_path = os.path.join(root_directory, subdir)
        if os.path.isdir(subdir_path): #文件夹判断
            zip_name = dtsdir + subdir + ".zip"
            with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(subdir_path):
                    if len(files) == 0:
                        for dir in dirs:
                            file_path = os.path.join(root,dir)
                            zip_info = zipfile.ZipInfo(os.path.relpath(file_path, root_directory) + '/') 
                            zipf.writestr(zip_info, b'')
                        continue
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, root_directory))
            print(f"压缩完成: {zip_name}")

if __name__ == "__main__":
    # 指定待压缩的目录路径
    root_directory = "inputs"
    dtedir = "inputs/"
    
    # 调用函数进行压缩
    zip_subdirectories(root_directory,dtedir)
