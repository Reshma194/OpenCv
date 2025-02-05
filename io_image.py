import cv2
#read image
image_path=r"C:\Users\DELL\Desktop\CV30\bird.jpg"
img=cv2.imread(image_path)
#write image
#visalize image
cv2.imshow('bird',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#wait until i press a key
