# Sketch

## General idea
Some simple code to do a "live sketch" with your webcam of whatever the webcam is facing.  There is also a function to turn any other image into a sketch of that image.  The code currently requires OpenCV and python to be installed on the computer previously.  I would like to improve this into an application which can be run on any computer in the future.

Simply running the code with "python sketch.py" will activate the webcam and open a window with the live sketch.

Calling the function "sketch_image" will ask for an image name, and then save that image with the same name plus the word sketch added to it.