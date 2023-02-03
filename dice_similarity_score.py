import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# Function for Dice Similarity Score
def dice(pred, true, k = 1):
    intersection = np.sum( pred[true==k] ) * 2.0
    dice = intersection / (np.sum(pred) + np.sum(true))
    return dice

# Variables for similarities
num_images = []
similarities = []
count = 0.5

# Load binary images 
calculated_masks_dir = "D:\Current Desktop\MSc\Computer Vision\Assessment\Task 1\GT_PYTHON"
ground_truth_masks_dir = "D:\Current Desktop\MSc\Computer Vision\Assessment\Task 1\GT\GT_Given"
calculated_mask_fn = os.listdir( calculated_masks_dir )
ground_truth_masks_fn = os.listdir( ground_truth_masks_dir )

for calculated_mask_file in calculated_mask_fn:

    gt_filepath = os.path.join( ground_truth_masks_dir, calculated_mask_file  )
    cal_filepath = os.path.join( calculated_masks_dir, calculated_mask_file  )

    if os.path.exists( gt_filepath ) and os.path.exists( cal_filepath ) : 

        gt = cv2.imread( gt_filepath ) 
        cal = cv2.imread( cal_filepath ) 

        if gt.shape[0] == cal.shape[0] and gt.shape[1] == cal.shape[1] : 
            # Calculating Dice Similarity Score    
            similarity = dice( cal, gt, k = 255 ) 
            similarities.append( similarity ) 
            num_images.append( count )
            count += 1
            
            # Resize images to view
            gt = cv2.resize( gt, (500, 500) ) 
            cal = cv2.resize( cal , (500, 500) ) 
            

# Save the values of similarities
similarities = np.array(similarities)
np.savetxt("Dice Similarity Score.csv", similarities, fmt= '%s', delimiter=",")

# Calculate mean, meedian and standard deviation
mean_sim = np.mean( similarities ) 
median_sim = np.median( similarities ) 
std_sim = np.std( similarities ) 

print ("Mean of similarities is {}".format(mean_sim))
print ("Median of similarities is {}".format(median_sim))
print ("Std. dev of similarities is {}".format(std_sim))

# Plot
fig = plt.figure(1, figsize=(10,10) ) 
plt.bar(num_images , similarities, width = 0.8 , bottom = None, color = "blue", edgecolor = "black")
plt.ylim([0.0, 1.0])
plt.title("Dice Similarity Scores with Mean: {0:0.2f} & Stadard Deviation: {0:0.3}".format(mean_sim, std_sim)) 
plt.xlabel("Number of Images")
plt.ylabel("Correpondig similarities of Images")
plt.show()