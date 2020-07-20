import numpy as np
from PIL import ImageGrab
import cv2
import time
from key import PressKey, ReleaseKey, W, A, S, D

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(org_img):
    processed_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1 = 200, threshold2 = 300)
    vertices = np.array([[10,599],[10,300], [800,300], [800, 599]])
    processed_img = roi(processed_img, [vertices])
    return processed_img

while(True):
    screen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    new_screen = process_img(screen)
    cv2.imshow('window',new_screen)
    # printscreen_numpy =  np.array(printscreen_pil.getdata(),dtype="uint8").reshape((printscreen_pil.size[1], printscreen_pil.size[0],3))
    # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

for i in range(4)[::-1]:
    print(i+1)
    time.sleep(1)

print('down')
PressKey(S)
time.sleep(3)
ReleaseKey(S)
print('up')
PressKey(W)
