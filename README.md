# Image-Segmentation-and-Detection

### Task 1: Object Segmentation
For each skin lesion image, I have applied Gaussian filter with Ostu threshold and then morphological filter (dilation_ with contour using OpenCV to automatically segment lesion object such as:
 
![b](https://user-images.githubusercontent.com/101992840/216715209-c9ec608a-c252-47f5-8b6a-dbeaf5c47abd.png)

### Task 2: Segmentation Evaluation
The task is to calculate the Dice Similarity (DS) Score of skin lesion dataset where M is the segmented lesion mask from Task 1 and M is the ground truth provided in the dataset [here](https://drive.google.com/drive/folders/1VWPGP18jjCaSucbnfN3ALRYAaPQxMPYU).

The equation to calculate DS score is:

![Screenshot 2023-02-03 132440](https://user-images.githubusercontent.com/101992840/216713606-a78e857f-e19c-433d-b007-86fab400f5ba.png)

### Results
To get the segmentation and DS score, run the python files with the dataset. The mean DS score is 0.8 with std. dev of 0.812 which is relatively better considering the data was not completely clean.
