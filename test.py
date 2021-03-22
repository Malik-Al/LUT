# from PIL import Image, ImageFilter
# img = Image.open('./image/img1.png')  # импортируем нужное изображения из папки
# data = img.getdata()  # возвращает содержимое этого изображения
# photoFil = [(d[0], d[2], d[1]) for d in data]  # примением цвета
# img.putdata(photoFil)  # копирует пиксельные данные в это изображение.
# img.save('./result_img/img.png')  # сохранения итогового изображения

from PIL import Image
from pillow_lut import load_cube_file
import os


# images = ['original1.png']
path = r'C:/Users/imeno/PycharmProjects/Color-t/image/'
images = os.listdir( path )


def transform(r, g, b):
    r, g, b = (max(r, g, b), g, min(r, g, b))
    avg_v = r * 0.2126 + g * 0.7152 + b * 0.0722
    r += (r - avg_v) * 0.3
    g += (g - avg_v) * 0.3
    b += (b - avg_v) * 0.3
    return r, g, b
# lut = load_cube_file('./test.cube')
lut = load_cube_file('./test2.cube.CUBE')


for image in images:
    Image.open('./input/' + image).filter(lut).save('./results/' + image)



