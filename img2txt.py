from paddleocr import PaddleOCR, draw_ocr
# Paddleocr `ch`, `en`, `french`, `german`, `korean`, `japan`。
ocr = PaddleOCR(use_angle_cls=True, use_gpu=False, lang="ch") # need to run only once to download and load model into memory
img_path = 'src_img/test.png'
result = ocr.ocr(img_path, cls=True)

filename = 'output.txt'
with open(filename, 'a', encoding='utf8') as file_object:
    for line in result:
        print(line[1][0])
        file_object.write(line[1][0] + "\n")



# display result
'''
from PIL import Image
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
txts = [line[1][0] for line in result]
scores = [line[1][1] for line in result]
im_show = draw_ocr(image, boxes, txts, scores, font_path='/path/to/PaddleOCR/doc/simfang.ttf')
im_show = Image.fromarray(im_show)
im_show.save('result.jpg')
'''
