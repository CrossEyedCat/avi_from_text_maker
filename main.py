import cv2
import numpy
from PIL import Image, ImageFont, ImageDraw
import sys

text=""
flag = True
for i in sys.argv[1:]:
    if flag:
        text=str(i)
        flag=False
    else:
        text=text+' '+str(i)
font = ImageFont.truetype("arial.ttf", size=20)
out = cv2.VideoWriter("video.avi", cv2.VideoWriter_fourcc('M','J','P','G'), 100, (100, 100))
for i in range(-100, 200):
    main_image = Image.new('RGB', (100, 100), 'black')
    idraw = ImageDraw.Draw(main_image)
    idraw.text((i, 40), text, font=font)
    opencvImage = cv2.cvtColor(numpy.array(main_image), cv2.COLOR_RGB2BGR)
    out.write(opencvImage)
out.release()
cv2.destroyAllWindows()
