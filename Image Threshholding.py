import cv2


image= cv2.imread("lena.jpg")

_,thr1 = cv2.threshold(image , 50,100 , cv2.THRESH_BINARY)
_,thr2 = cv2.threshold(image , 200,255,cv2.THRESH_BINARY_INV)
_,thr3 = cv2.threshold(image , 200,255,cv2.THRESH_TOZERO)
_,thr4 = cv2.threshold(image , 200,255,cv2.THRESH_TOZERO_INV)




cv2.imshow("Original image" , image)
cv2.imshow("Binary" , thr1)
cv2.imshow("Binary Inverse" , thr2)
cv2.imshow("ToZero" , thr3)
cv2.imshow("ToZero Inverse " , thr4)



cv2.waitKey(0)
cv2.destroyAllWindows()