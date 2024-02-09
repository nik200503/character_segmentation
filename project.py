import cv2
import numpy as np
# loading images
img1 = cv2.imread("/home/nik2005/Pictures/Screenshots/E.png")
img2 = cv2.imread("/home/nik2005/Pictures/Screenshots/B.jpeg")
img3 = cv2.imread("/home/nik2005/Pictures/Screenshots/C.jpeg")
img4 = cv2.imread("/home/nik2005/Pictures/Screenshots/C2.jpeg")
img5 = cv2.imread("/home/nik2005/Pictures/Screenshots/N.jpeg")
img6 = cv2.imread("/home/nik2005/Pictures/Screenshots/M.jpeg")
img7 = cv2.imread("/home/nik2005/Pictures/Screenshots/F.jpeg")

img = [img1,img2,img3,img4,img5,img6,img7]

#hsv
img_hsv=[]
for i in range(0,len(img)):
        a=chr(i)
        b= 'img' + a + '_hsv'
        b=cv2.cvtColor(img[i],cv2.COLOR_BGR2HSV)
        img_hsv.append(b)
 

#smoothing
img_smooth=[]
lower_red = np.array([0,0,0])
upper_red = np.array([255,255,255])
for i in range(0, len(img_hsv)):
    a= chr(i)
    d= 'img' + a + '_smooth'
    mask = cv2.inRange(img_hsv[i], lower_red , upper_red)
    res = cv2.bitwise_and(img[i] ,img[i] , mask=mask )
    d=cv2.medianBlur(res, 5)
    img_smooth.append(d)


img_gray=[]
# converting the images to grayscale
for i in range(0 ,len(img)):
    a=chr(i)
    b='img'+ a + '_gray'
    b = cv2.cvtColor(img_smooth[i] , cv2.COLOR_BGR2GRAY)
    img_gray.append(b)


#showing the images
for i in range(0,len(img_gray)):
    a=chr(i)
    b='img' + a + '_smooth'
    cv2.imshow(b ,img_gray[i] )

#thresholding
img_threshold=[]
for i in range(0,len(img_smooth)):
    a=chr(i)
    b= 'img' + a + '_thresholding'
    b=cv2.adaptiveThreshold(img_gray[i], 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 21 , 11)
    img_threshold.append(b)

#showing the images
for i in range(0,len(img_gray)):
    a=chr(i)
    b='img' + a + '_smooth'
    cv2.imshow(b ,img_threshold[i] )


cv2.waitKey(0)
cv2.destroyAllWindows()
