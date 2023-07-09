import cv2

img = cv2.imread("D:\PYTHON\QT\img.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)

cv2.imshow("Image",img)
cv2.imshow("Image Gray",imgGray)
cv2.imshow("Image blur",imgblur)
cv2.imshow("Image Canny", imgCanny)

cv2.waitKey(0)