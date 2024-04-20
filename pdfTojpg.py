import os
import fitz

def extract_images_from_pdf(pdf_path, output_folder):
    # 打开PDF文件
    pdf_document = fitz.open(pdf_path)

    # 创建以PDF文件名命名的文件夹
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    pdf_output_folder = os.path.join(output_folder, pdf_name)
    os.makedirs(pdf_output_folder, exist_ok=True)

    # 遍历PDF的每一页
    for page_number in range(0,len(pdf_document)):
        page = pdf_document.load_page(page_number)

        # 提取页面中的图片
        images = page.get_images(full=True)
        
        # 遍历页面中的每一张图片
        for img_index, img in enumerate(images):
            # 获取图片的XREF，用于提取图片数据
            xref = img[0]

            # 提取图片数据
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            # 构建图片文件名
            image_filename = f"{output_folder}/{pdf_name}/{page_number:04d}_{img_index}.{image_ext}"

            # 保存图片到指定文件夹
            with open(image_filename, "wb") as image_file:
                image_file.write(image_bytes)

    # 关闭PDF文件
    pdf_document.close()

def process_pdf_folder(pdf_folder, output_folder):
    # 遍历PDF文件夹中的所有PDF文件
    for root, _, files in os.walk(pdf_folder):
        for file in files:
            if file.endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                # 对每个PDF文件进行处理
                extract_images_from_pdf(pdf_path, output_folder)

# 指定PDF文件夹和输出文件夹
pdf_folder_path = "./inputs"  # PDF文件夹路径
output_folder_path = "./inputs"  # 输出文件夹路径

# 调用函数处理PDF文件夹中的所有PDF文件
process_pdf_folder(pdf_folder_path, output_folder_path)
