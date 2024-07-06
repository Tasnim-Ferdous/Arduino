import cv2

logo = cv2.imread("Logo.png")

cv2.imshow("Logo.png", logo)
cv2.imwrite("Logo.jpeg", logo)

cv2.waitKey()
cv2.destroyAllWindows()