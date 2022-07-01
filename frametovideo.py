path ="pred1"
from PIL import Image
import glob
image_list = []
k=0
import cv2
frameSize = (448, 448)
out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 25, frameSize)

frame1=[]

imgpath=[]

for filename in glob.glob("pred1/*.jpg"):
    imgpath.append(filename)

imgpath.sort()

for filename in imgpath: #assuming gif
    # print(filename)
    # image = Image.open(filename)
    image=cv2.imread(filename)
    # image.show()
    # cv2.imshow("pp",image)
    height, width, layers = image.shape
    frameSize = (width,height)
    frame1.append(image)
    # out.write(image)
    #image=Image.open(filename)
    #image=cv2.imread(filename)
    # image_list.append(im)

# print(frame1[0])
out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'DIVX'), 3, frameSize)

for i in frame1:
    out.write(i)

out.release()



