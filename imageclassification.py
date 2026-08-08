"""CNN Image Classification using Python (TensorFlow/Keras)

This experiment demonstrates how to perform image classification using a Convolutional Neural Network (CNN). The example uses the CIFAR-10 dataset, which contains 60,000 color images belonging to 10 classes.

Aim

To implement a Convolutional Neural Network (CNN) for image classification using Python, TensorFlow, and Keras.

Theory

A Convolutional Neural Network (CNN) is a deep learning algorithm designed specifically for processing images. It automatically extracts features such as edges, textures, and shapes to classify images.


CNN arch 

            Input Image (32×32×3)
                     │
                     ▼
        Convolution Layer (32 Filters)
                     │
                     ▼
            ReLU Activation
                     │
                     ▼
             Max Pooling (2×2)
                     │
                     ▼
        Convolution Layer (64 Filters)
                     │
                     ▼
            ReLU Activation
                     │
                     ▼
             Max Pooling (2×2)
                     │
                     ▼
                Flatten Layer
                     │
                     ▼
          Fully Connected Layer (64)
                     │
                     ▼
             Output Layer (10 Classes)
Requirements

Install TensorFlow and Matplotlib:

pip install tensorflow matplotlib numpy

Verify installation:

import tensorflow as tf
print(tf.__version__)

"""


#pip install tensorflow matplotlib numpy


import tensorflow as tf
print(tf.__version__)


import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# ----------------------------------------
# Load CIFAR-10 Dataset
# ----------------------------------------

(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize images (0-255 → 0-1)

train_images = train_images / 255.0
test_images = test_images / 255.0

# Class names

class_names = [
    'Airplane',
    'Automobile',
    'Bird',
    'Cat',
    'Deer',
    'Dog',
    'Frog',
    'Horse',
    'Ship',
    'Truck'
]

# ----------------------------------------
# Display Sample Images
# ----------------------------------------

plt.figure(figsize=(10,5))

for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(train_images[i])
    plt.title(class_names[train_labels[i][0]])
    plt.axis("off")

plt.show()

# ----------------------------------------
# Build CNN Model
# ----------------------------------------

model = models.Sequential()

model.add(layers.Conv2D(32,(3,3),activation='relu',
                        input_shape=(32,32,3)))

model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64,(3,3),activation='relu'))

model.add(layers.MaxPooling2D((2,2)))

model.add(layers.Conv2D(64,(3,3),activation='relu'))

model.add(layers.Flatten())

model.add(layers.Dense(64,activation='relu'))

model.add(layers.Dense(10,activation='softmax'))

# ----------------------------------------
# Compile Model
# ----------------------------------------

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# ----------------------------------------
# Train Model
# ----------------------------------------

history = model.fit(
    train_images,
    train_labels,
    epochs=10,
    validation_data=(test_images,test_labels)
)

# ----------------------------------------
# Evaluate Model
# ----------------------------------------

test_loss, test_accuracy = model.evaluate(
    test_images,
    test_labels
)

print("\nTest Accuracy:",test_accuracy)

# ----------------------------------------
# Predict One Image
# ----------------------------------------

prediction = model.predict(test_images[:1])

predicted_class = prediction.argmax()

print("Predicted :",class_names[predicted_class])

print("Actual :",class_names[test_labels[0][0]])

plt.imshow(test_images[0])
plt.title("Prediction : "+class_names[predicted_class])
plt.axis("off")
plt.show()



'''Sample Output

Training:

Epoch 1/10

1563/1563
loss: 1.47
accuracy: 0.46

Epoch 2/10

accuracy: 0.61

Epoch 5/10

accuracy: 0.73

Epoch 10/10

accuracy: 0.80

Evaluation:

Test Accuracy:

0.79

Prediction:

Predicted : Airplane

Actual : Airplane
Model Summary
Layer (type)              Output Shape

Conv2D                    (30,30,32)

MaxPooling2D              (15,15,32)

Conv2D                    (13,13,64)

MaxPooling2D              (6,6,64)

Conv2D                    (4,4,64)

Flatten                   (1024)

Dense                     (64)

Dense                     (10)
Workflow
Image Dataset
      │
      ▼
Load Images
      │
      ▼
Normalize Images
      │
      ▼
CNN Layers
      │
      ▼
Feature Extraction
      │
      ▼
Flatten
      │
      ▼
Dense Layer
      │
      ▼
Softmax Output
      │
      ▼
Predicted Class
Advantages of CNN
Automatically extracts image features.
High accuracy for image classification tasks.
Handles large image datasets efficiently.
Widely used in computer vision applications.
Applications
Face Recognition
Medical Image Analysis
Object Detection
Self-Driving Cars
Traffic Sign Recognition
Handwritten Digit Recognition
Plant Disease Detection
Time Complexity

For one convolutional layer:

Time Complexity: O(H × W × K² × C × F)

Where:

H = Image height
W = Image width
K = Kernel size
C = Number of input channels
F = Number of filters'''