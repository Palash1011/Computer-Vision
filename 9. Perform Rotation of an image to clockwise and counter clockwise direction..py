import cv2
path=r"C:\Users\palas\OneDrive\Pictures\Screenshots\Screenshot 2024-02-21 090822.png"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_180)
cv2.imshow(window_name, image)
cv2.waitKey(0)
