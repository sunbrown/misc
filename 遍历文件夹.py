import os
from PIL import Image
from tqdm import tqdm

for filename in tqdm(os.listdir(r'F:\jpg')):
    img = Image.open(r'F:\jpg\{}'.format(filename)).convert('RGB')
    img.save(r'F:\jpg1\{}'.format(filename))
