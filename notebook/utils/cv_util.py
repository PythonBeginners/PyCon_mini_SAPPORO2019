import cv2
import matplotlib.pyplot as plt

# RGBを正しい値に変換して画像を読み込む
def read_image_rgb (path:str):
    img_src = cv2.imread(path, 1)
    img_src = cv2.cvtColor(img_src, cv2.COLOR_BGR2RGB)
    return img_src

# 画像を表示
def show_color(obj, figsize=(14, 11)):
    fig, ax = plt.subplots(figsize=figsize)
    plt.imshow(obj)  #貼り付け
    plt.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False) # ラベルを削除する
    plt.tick_params(bottom=False, left=False, right=False, top=False) # 目盛りを削除する
    plt.show()

# tesseract_ocrの返すbox情報をimageに書き込む    
def draw_tesseract_boxes(img_temp, tesseract_boxes, color=(255,0,0)):
    for box_index in range(len(tesseract_boxes)):
        tesseract_box = tesseract_boxes[box_index]
        left = tesseract_box.position[0][0]
        top = tesseract_box.position[0][1]
        right = tesseract_box.position[1][0]
        bottom = tesseract_box.position[1][1]
        
        if left > 0 and top > 0: ## left, top が両方ゼロで不正な値が入ることがあるため除外する
            cv2.rectangle(img_temp, (left, top), (right,bottom), color, 2)
    return img_temp    