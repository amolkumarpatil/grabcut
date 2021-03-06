import cv2
import numpy as np 
import time
import os 
import hog_detector 
import imutils
im_path = input("Enter input image path: ")
im = cv2.imread(im_path)
im = imutils.resize(im, width=min(400, im.shape[1]))
# im = "C:/Users/Amol/Pictures/sample.jpg"


# bounding box of detected object
rect = hog_detector.pedestrian_detection(im)
mask = np.zeros(im.shape[:2], dtype="uint8")
# # bounding box of detected object
# rect = (153, 17, 231, 189)

# below numpy arrays are used for segmenting foreground and background for cv2.grabcut
fgModel = np.zeros((1, 65), dtype="float")
bgModel = np.zeros((1, 65), dtype="float")

# apply GrabCut using the the bounding box segmentation method
# time is used to note the timings as grabcut method runs on given iterations it may vary based on resolution and bb
start = time.time()
(mask, bgModel, fgModel) = cv2.grabCut(im, mask, rect, bgModel,
	fgModel, iterCount=60, mode=cv2.GC_INIT_WITH_RECT)
end = time.time()

print("time taken to run grabcut:", (start-end))

# mask variable will have 4 output values for masks. Let's define these in a tuple and iterate it over masks
# If mask value matches our given value, it will be stored in valueMask variable.
values = (
	("Definite Background", cv2.GC_BGD),
	("Probable Background", cv2.GC_PR_BGD),
	("Definite Foreground", cv2.GC_FGD),
	("Probable Foreground", cv2.GC_PR_FGD),
)

# loop over the possible GrabCut mask values
for (name, value) in values:
	# construct a mask that for the current value
	print("[INFO] showing mask for '{}'".format(name))
	valueMask = (mask == value).astype("uint8") * 255
	# display the mask so we can visualize it
	cv2.imshow(name, valueMask)
	cv2.waitKey(0)

# Let's set all background pixels to 0 i.e. black and all foreground pixels to 1 i.e. white
outputMask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD),0, 1)
# scale the mask from the range [0, 1] to [0, 255]
outputMask = (outputMask * 255).astype("uint8")
# apply a bitwise AND to the image using our mask generated by
# GrabCut to generate our final output image
output = cv2.bitwise_and(im, im, mask=outputMask)

cv2.imshow("Input", im)
cv2.imshow("GrabCut Mask", outputMask)
cv2.imshow("GrabCut Output", output)
cv2.waitKey(0)