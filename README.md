This project is implementation of segmentation technique in computer vision which is called as grabcut.

Grabcut extracts foreground from background of an image using Gaussian Mixture model.

Refer https://docs.opencv.org/3.4/d8/d83/tutorial_py_grabcut.html for more details.

# Methods
1. Bounding Box based initialization

In this method, a bounding box of interested region must be initialized in order to run the grabcut algorithm.

Bounding box of object is automatically detected using HoG detector. Currently Hog is classifier is implemented using SVM for pedestrian class and can be extended further to add more classes.


 There can be many methods to initialize bounding box :-
* Manual labeling of coordinates
* Using Feature extractor like HoG or SVM
* CNN based detector like RCNN or YOLO

# To Do

* Mask based initialization grabcut
