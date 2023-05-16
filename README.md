[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FBakar31%2FBMW-Hackathon&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# Object Detection for Industrial Use-Cases: BMW SORDI Hackathon

## A Student's Approach with Limited Hardware Resources

**Note:** I did this project as a participant of **BMW SORDI.ai Hackathon 2022** organized by **HackerEarth**.

**Rank: 25th Place among 636 teams**

**Team Name:** MockingBird (Solo)

## Introduction:

The SORDI.ai Hackathon 2022 challenged participants to build object detection models for real-world BMW use cases using the Synthetic Object Recognition Dataset for Industries (SORDI). The dataset consists of hundreds of thousands of photo-realistic images for 80+ distinct object classes highlighting logistics, transportation, signage, tools, and office assets. The aim of the competition was to popularize the SORDI dataset and enhance computer vision tasks in digital-twin environments.

## Objectives:

- Utilize the SORDI dataset, consisting of synthetic visual industrial assets, to train object detection models.
- Achieve high accuracy levels in detecting and recognizing objects relevant to industrial domains, such as logistics, transportation, signage, tools, and office assets.
- Showcase the practical applicability of AI-based computer vision solutions for real-world BMW use-cases.

## Approach:

### Dataset Selection: 
Due to limited hardware resources, a strategic approach was taken to select a smaller subset of images and labels from each class within the SORDI dataset. A Python script was utilized to extract a small number of representative samples from each class. This step ensured that the training process would be manageable and feasible given the hardware limitations. But it cost me the accuray and leaderboard.

### Data Conversion: 
The selected images and corresponding labels were converted into the YOLO format, which is widely used for object detection tasks. This format provides bounding box coordinates and class labels for each object in the image.

### YOLO Model Selection: 
Considering the hardware constraints, **YOLOv5** was chosen as the object detection model for training. While YOLOv7 is known to offer improved results, YOLOv5 was deemed more suitable for the available hardware resources.

### Training: 
The training process was carried out on the Kaggle platform, which provided the necessary computational resources to train the YOLOv5 model. Kaggle's infrastructure helped mitigate the hardware restrictions and allowed for the efficient training of the object detection model.

### Hyperparameter Selection: 
The hyperparameters were carefully selected to optimize the training process within the available hardware resources. The model was trained for **50 epochs**, with a **batch size of 16** and an **image size of 1280**. A **learning rate of 0.01** was used to facilitate effective optimization of the model during training.

Evaluation and Results: The trained model was evaluated on a separate test dataset to assess its performance in object detection. Metrics such as precision, recall, and mean average precision (mAP) were used to measure the model's accuracy and effectiveness.

## Result:
 - Score: 25.49859 
 - [LeaderBoard](https://www.hackerearth.com/challenges/competitive/SORDI-ai-hackathon-2022/leaderboard/) : 25th among 636 teams/participants

### P-curve
 ![alt text](https://github.com/Bakar31/BMW-Hackathon/blob/master/P_curve.png)

 ### R-curve
 ![alt text](https://github.com/Bakar31/BMW-Hackathon/blob/master/R_curve.png)

 ### confusion_matrix
 ![alt text](https://github.com/Bakar31/BMW-Hackathon/blob/master/confusion_matrix.png)


**Despite the hardware limitations, the decision was made to not quit the competition but rather to embrace the challenge and explore alternative approaches. This mindset allowed me for valuable learning experiences and the opportunity to adapt to real-world scenarios with limited resources.**

## Conclusion:

The approach taken in this hackathon showcased resilience and determination in the face of hardware limitations. By selecting a smaller subset of the SORDI dataset and training the YOLOv5 model on Kaggle, competitive results were achieved despite the constraints. This experience demonstrates the importance of perseverance and the ability to adapt to challenges in order to participate and succeed in real-world AI competitions.


