import cv2
import matplotlib.pyplot as plt

# RGBを正しい値に変換して画像を読み込む
def read_image (path:str):
    im_cv = cv2.imread(test_path, 1)
    img_src = cv2.cvtColor(im_cv, cv2.COLOR_BGR2RGB)
    return img_src

# 画像を表示
def show_color(obj, figsize=(14, 11)):
    fig, ax = plt.subplots(figsize=figsize)
    plt.imshow(obj)  #貼り付け
    plt.show()