import os, shutil
from PIL import Image
from tqdm import tqdm

# # --------只遍历当前目录下的文件，不包括子文件夹----------
# for filename in tqdm(os.listdir(r'F:\jpg')):
#     img = Image.open(r'F:\jpg\{}'.format(filename)).convert('RGB')
#     img.save(r'F:\jpg1\{}'.format(filename))


# # -------遍历所有的目录和文件，包括子文件夹------------)
# for read_path, dirs, files in os.walk(r"D:/greyimage"):
#     for file in files:
#         print(os.path.join(read_path, file))
