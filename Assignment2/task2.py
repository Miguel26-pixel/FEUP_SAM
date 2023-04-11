import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the input image
background_img = cv2.imread('Assignment2/images/christmasBB.jpg')
img = cv2.imread('Assignment2/images/download2.jpg')

# separate each RGB component into a different matrix
B, G, R = cv2.split(img)

# compute the blueness of each pixel using the equation blueness = B - max(R,G)
blueness = np.subtract(B.astype(np.float64), np.maximum(R,G))

plt.hist(blueness.ravel(), 256, [np.min(blueness), np.max(blueness)])
plt.show()

# select a threshold based on the blueness factor
threshold = int(input("Threshold? "))

# create a new black and white image with the foreground objects with value 255
# and all other pixels with value 0
mask = np.zeros_like(B)
mask[blueness < threshold] = 255

plt.imshow(mask, cmap="gray")
plt.show()

foreground_bl = cv2.bitwise_and(img, img, mask=mask.astype(np.uint8))
plt.imshow(cv2.cvtColor(foreground_bl, cv2.COLOR_BGR2RGB))
plt.title('Colored foreground using blueness');
plt.show()

background_img_resized = cv2.resize(background_img, (foreground_bl.shape[1], foreground_bl.shape[0]))

blackPixel = [0, 0, 0]
print(foreground_bl[0][0])
if(all(foreground_bl[0][0] == blackPixel)): print("equal") 
else: print("not")

blended = cv2.addWeighted(background_img_resized, 0.5, foreground_bl, 1, 0.0)
print(foreground_bl.shape)

for line in range(background_img_resized.shape[0]):
    for pixel in range(background_img_resized.shape[1]):
        if(all(foreground_bl[line][pixel] != blackPixel)): 
            background_img_resized[line][pixel] = foreground_bl[line][pixel]

cv2.imshow('Original Image', img)
cv2.imshow('Segmented Image', blended)
cv2.imshow('Segmented Image Manual Join', background_img_resized)
cv2.waitKey(0)

cv2.imwrite('segmented_image_manual_join.jpg', background_img_resized)
cv2.imwrite('segmented_image.jpg', blended)