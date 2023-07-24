import cv2
import numpy as np
screen = cv2.VideoCapture(0)
img_mask = cv2.imread('directory/1.JPG')
img_mask = cv2.resize(img_mask, (500, 500), interpolation=cv2.INTER_AREA)

while True:
    ret, frame = screen.read()
    if ret == 0:
        break
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (500, 500), interpolation=cv2.INTER_AREA)
    # HSV renk uzayına dönüştürelim
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # HSV renk aralığına göre yeşil rengi seçelim
    hsvGreenColor = cv2.inRange(frame_HSV, (0, 157, 165), (255, 255, 255))

    mask = cv2.bitwise_not(hsvGreenColor)
    show = cv2.bitwise_and(img_mask, img_mask, mask=hsvGreenColor)
    bulanık=cv2.blur(frame,(15,15))
    show = np.where(show == 0, bulanık, show)


    cv2.imshow("Orjinal", frame)
    cv2.imshow("GreenSelect", hsvGreenColor)
    cv2.imshow("Foto",img_mask)
    cv2.imshow("blurs", show)


    # 'q' tuşuna basıldığında döngüyü sonlandıralım
    if cv2.waitKey(200) & 0xFF == ord("q"):
        break
# Pencereleri kapatalım ve kaynakları serbest bırakalım
cv2.destroyAllWindows()