import argparse
import cv2
from pprint import pprint
import numpy as np
import pandas as pd

def detectCircles(i_image, colored_image):
	blur = cv2.medianBlur(i_image,5)
	circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.1109, 30)
	circles = np.uint16(np.around(circles))
	for i in circles[0,:]:
	    # draw the outer circle
	    cv2.circle(colored_image,(i[0],i[1]),i[2],(0,255,0),2)
	    # draw the center of the circle
	    cv2.circle(colored_image,(i[0],i[1]),1,(0,0,255),2)

	cv2.imshow('detected circles',colored_image)

image = cv2.imread("coins.jpg", cv2.IMREAD_COLOR)
cimg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.namedWindow("coins", cv2.WINDOW_KEEPRATIO)
# print('teste')
while True:
	cv2.imshow("coins", image.astype('uint8'))
	key = cv2.waitKey(1) & 0xFF
	if key == ord("d"):
		detectCircles(cimg, image)
	elif key == ord("c"):
		break
cv2.destroyAllWindows()
