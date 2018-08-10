import cv2
import numpy as np

# Our sketch generating function
def sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    # Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 40)
    #cv2.imshow('Live Canny', canny_edges)
    
    # Do an invert binarize the image 
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask


def sketch_image():
    image_name = input("Please Write the image name.")

    image = cv2.imread(image_name,0)

    # Convert image to grayscale
    #img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(image, (5,5), 0)

    print("Is this function being run?")

    # Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 100)
    cv2.imshow('Live Canny', canny_edges)

    # Do an invert binarize the image 
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('InverseCanny', mask)

    name_list = image_name.split(str=".")

    image_name = name_list[0]+ "_sketch." + name_list[1]

    imwrite(image_name, gray_image);

    cv2.waitKey()

    cv2.destroyAllWindows()

def main():
    # Initialize webcam, cap is the object provided by VideoCapture
    # It contains a boolean indicating if it was sucessful (ret)
    # It also contains the images collected from the webcam (frame)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow('Our Live Sketcher', sketch(frame))
        if cv2.waitKey(1) == 13: #13 is the Enter Key
            break
            
    # Release camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()