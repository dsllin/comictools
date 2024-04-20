import os

# 指定文件夹路径
folder_path = 'outputs'

# 遍历文件夹内的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.jpeg'):  # 如果文件名以 ' ' 结尾
        # 提取文件名中下划线前的部分
        # category = "碧蓝之海第"+filename.split('_')[1]+"卷"
        category = filename.split('_')[0]#+ "_" +filename.split('_')[1]
        delname = filename.split('_')[0]+ "_" #+filename.split('_')[1]+'_'
        
        #使用utf-8编码时的解码还原，转换非英文字符方便图片处理
        # category = category.replace("u","\\u")
        # category = bytes(category, 'utf-8').decode('unicode_escape')

        print(category)
        
        # 构建分类文件夹的路径
        category_folder = os.path.join(folder_path, category)
        
        # 检查分类文件夹是否存在，如果不存在则创建它
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        
        # 构建文件的源路径和目标路径
        ffilename = filename.replace(delname, '')
        source_file_path = os.path.join(folder_path, filename)
        destination_file_path = os.path.join(category_folder, ffilename)
        
        # 移动文件到分类文件夹中
        os.rename(source_file_path, destination_file_path)
