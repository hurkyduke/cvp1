import cv2
import numpy as np

# Create a black image (all zeros) with dimensions 500x500 and 3 channels (RGB)
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Draw a blue rectangle on the image
cv2.rectangle(image, (100, 100), (400, 400), (255, 0, 0), -1)  # -1 fills the rectangle with color

# Draw a green circle on the image
cv2.circle(image, (250, 250), 50, (0, 255, 0), -1)  # -1 fills the circle with color

cv2.rectangle(image , (120,120),(200,200),(0,0,211),-1)
# Save the image
cv2.imwrite('output_image.png', image)

# Display the image
cv2.imshow('2D Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

