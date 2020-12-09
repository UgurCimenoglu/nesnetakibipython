import cv2 #OpenCv ekleme
import numpy as np #numpy ekleme

def nothing(x): # boş bir fonksiyon gerekli imiş.
    pass
cv2.namedWindow("Tracking") #yeni bir window oluşturma
cv2.createTrackbar("LH","Tracking",0,255,nothing) #Trackbar oluşturuyoruz
cv2.createTrackbar("LS","Tracking",0,255,nothing)#Trackbar oluşturuyoruz
cv2.createTrackbar("LV","Tracking",0,255,nothing)#Trackbar oluşturuyoruz
cv2.createTrackbar("UH","Tracking",255,255,nothing)#Trackbar oluşturuyoruz
cv2.createTrackbar("US","Tracking",255,255,nothing)#Trackbar oluşturuyoruz
cv2.createTrackbar("UV","Tracking",255,255,nothing)#Trackbar oluşturuyoruz

cap = cv2.VideoCapture(0) #Webcam Görüntüsünü alıyorum ve cap değişkenine atıyorum
while True: # True Olduğu sürece
    ret,frame=cap.read() #Webcam Görüntüsünü Okuyoruz.
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # BGR formatından HSV formatına dönüştürüyorum.

    lh = cv2.getTrackbarPos("LH","Tracking") #Trackbaar Değerlerini Get ediyoyoruz, alıyoruz
    lv = cv2.getTrackbarPos("LS", "Tracking")#Trackbaar Değerlerini Get ediyoyoruz, alıyoruz
    ls = cv2.getTrackbarPos("LV", "Tracking")#Trackbaar Değerlerini Get ediyoyoruz, alıyoruz
    uh = cv2.getTrackbarPos("UH", "Tracking")#Trackbaar Değerlerini Get ediyoyoruz, alıyoruz
    us = cv2.getTrackbarPos("US", "Tracking")#Trackbaar Değerlerini Get ediyoyoruz, alıyoruz
    uv = cv2.getTrackbarPos("UV", "Tracking")#Trackbaar Değerlerini Get ediyoyoruz, alıyoruz
    lower_hsv = np.array([lh, ls, lv], np.uint8) #lower_hsv değişkenine trackbardaki low değerlerini atıyoruz.
    upper_hsv = np.array([uh, us, uv], np.uint8) #upper_hsv değişkenine trackbardaki up değerlerini atıyoruz.
    mask=cv2.inRange(hsv,lower_hsv,upper_hsv) #Sayısal değerleri alıyoruz.
    result=cv2.bitwise_and(frame,frame,mask=mask) #sonuc olarak trackbardaki değerleri kameraya uyguluyoruz.
    cv2.imshow("deneme", result)#Görüntüyü ekrana çıkartıyoruz.

    if cv2.waitKey(1) & 0xFF == ord('q'): # q ya bastığımız zaman kapansın.
        break

cap.release()
cv2.destroyAllWindows()