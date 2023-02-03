import cv2 
import numpy as np
import os 

GT_DIR = "D:\Current Desktop\MSc\Computer Vision\Assessment\Task 1\GT_PYTHON"
BASE_DIR = "D:\Current Desktop\MSc\Computer Vision\Assessment\Task 1\org data"
images_filename = os.listdir( BASE_DIR ) 

RESIZE_WIDTH = 300

if not os.path.exists(GT_DIR):
    os.mkdir( GT_DIR )

for image_filename in images_filename: 

    try: 
        # read images
        img_resized = cv2.imread( os.path.join( BASE_DIR , image_filename ) )
        # convert to gray scale and then binary image
        gray_img = cv2.cvtColor( img_resized, cv2.COLOR_BGR2GRAY )
        # Otsu's thresholding after Gaussian filtering
        blur_img = cv2.GaussianBlur(gray_img,(3,3),0)
        ret3, binary_img = cv2.threshold(blur_img ,0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        # apply morphological filter (dilation) 
        kernel = np.ones((3,3),np.uint8)
        dilation_img = cv2.dilate(binary_img.copy(), kernel, iterations = 5)
        dilation_img = 255 - dilation_img 
        contours, hierarchy = cv2.findContours(dilation_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnt_img = np.zeros( (img_resized.shape[:2]) , dtype = np.uint8 )

        for cnts in contours:
            (x,y),radius = cv2.minEnclosingCircle(cnts)
            center = (int(x),int(y))
            radius = int(radius)
            areaCnt = cv2.contourArea(cnts) 
            h, w = img_resized.shape[:2]
            areaImg = h * w

            if (areaCnt < 0.65 * areaImg) and (areaCnt > 0.0075 * areaImg) and (x > 0.2 * w) and (x < 0.8 * w): # and (y > 0.2*h) and (y < 0.2*h):    
                cv2.circle(img_resized,center,radius,(255,255,0),2)
                cv2.drawContours( cnt_img, [cnts], -1, (255, 0, 0 ), -1 ) 
                cv2.drawContours(img_resized, [cnts], -1, (0,255,0), 3)
                break
    
        # save images
        png_filename = image_filename.split(".")[0]
        # cv2.imwrite( os.path.join( GT_DIR, png_filename + "_gray.png"), gray_img )
        # cv2.imwrite( os.path.join( GT_DIR, png_filename + "_binary.png"), dilation_img )
        cv2.imwrite( os.path.join( GT_DIR, png_filename + "_Segmentation.png"), cnt_img )

    # handle keyboard interrupt
    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break 
    
