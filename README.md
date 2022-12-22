# BMW-Hackathon

# Team Name: Mocking Bird (Solo)

## Goal:
The goal of this competetion was to build an object detection model for industrial use-cases. 

## My approach:
The given dataset was huge. As I am a student, I don't have the kind of hardware that this competition needs. But I surely can't run away from a challenge. So, I tried another approach. I selected a small number of images and labels from each class using a Python script, then converted them into the Yolo format. The code for these steps can be found in the `src` folder.Even with such a small number of images, I encountered numerous difficulties.Every challenge is an opportunity to learn new things. It was a great opportunity for me to get used to the real-world scenerio.

I used `yolov5` for my hardware restriction, but `yolov7` will give much better results.

- img_size: 1280 
- batch_size: 16 
- epochs 50:
- lr: 0.01
- nc: 17 

## Result:
 - Score: 25.49859 
 - [LeaderBoard](https://www.hackerearth.com/challenges/competitive/SORDI-ai-hackathon-2022/leaderboard/) : 25th among 636 teams/participants

### P-curve
 ![alt text](https://github.com/Bakar31/BMW-Hackathon/blob/master/P_curve.png)

 ### R-curve
 ![alt text](https://github.com/Bakar31/BMW-Hackathon/blob/master/R_curve.png)

 ### confusion_matrix
 ![alt text](https://github.com/Bakar31/BMW-Hackathon/blob/master/confusion_matrix.png)