from PIL import Image
import wordcloud
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def ciyvn(str):
    img_codemao =np.array(Image.open('codemao.png'))
    w=wordcloud.WordCloud(mask = img_codemao,font_path='fangzheng.TTF',background_color='white',
                          max_words=2000,width=2000,height=2000)
    w.generate(str)
    image_colors = wordcloud.ImageColorGenerator(image = img_codemao)
    w.recolor(color_func =image_colors)
    w.to_file('shortstory.png')
    img = Image.open('shortstory.png')
    return img

