import cv2
import numpy as np

# Read the input image
img = cv2.imread('Assignment2/images/jump.jpg')

# separate each RGB component into a different matrix
B, G, R = cv2.split(img)

# compute the blueness of each pixel using the equation blueness = B - max(R,G)
blueness = np.subtract(B, np.maximum(R,G))

# select a threshold based on the blueness factor
threshold = 100
threshold2 = 210

# create a new black and white image with the foreground objects with value 255
# and all other pixels with value 0
mask = np.zeros_like(B)
mask[blueness > threshold] = 255
mask_3c = cv2.merge((mask, mask, mask))

mask2 = np.zeros_like(B)
mask2[blueness > threshold2] = 255
mask_3c2 = cv2.merge((mask2, mask2, mask2))
# Invert the mask
inv_mask = cv2.bitwise_not(mask)
inv_mask2 = cv2.bitwise_not(mask2)

# Create a blue background image
blue_bg = np.zeros_like(img)
blue_bg[:, :, 0] = 255

# Set the alpha values for each image
alpha_fg = mask.astype('float32') / 255.0
alpha_bg = inv_mask.astype('float32') / 255.0

blended = cv2.addWeighted(img, 1.0, blue_bg, 1.0, 0.0)

# Apply the mask to the blended image
result = cv2.bitwise_and(blended, blended, mask=mask)

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow('Segmented Image', result)
cv2.waitKey(0)

# Save the segmented image
cv2.imwrite('segmented_image.jpg', result)