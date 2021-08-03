import cv2
import numpy as np


if __name__ == '__main__':
    img = cv2.imread("/home/bb6/Pictures/qrcode.jpeg")
    cv2.imshow("QR", img)
    cv2.waitKey()

    height, width = img.shape[:2]
    M = cv2.getRotationMatrix2D((width/2, height/2), 45, 0.5)
    rot = cv2.warpAffine(img,M,(width,height))
    cv2.imshow("rotate", rot)
    cv2.waitKey()

    detector = cv2.wec
    qr = cv2.QRCodeDetector()
    data,box,sqrcode = qr.detectAndDecode(rot)
    print(box)
    x1 = int(box[0][0][0])
    y1 = int(box[0][0][1])
    x2 = int(box[0][2][0])
    y2 = int(box[0][2][1])
    print(box)
    box = np.int0(box)
    box1 = np.int8(box)
    cv2.drawContours(rot, [box], 0, (255,0,0),2)
    print(data)
    cv2.imshow("codebox", rot)
    cv2.waitKey()
    cv2.destroyAllWindows()