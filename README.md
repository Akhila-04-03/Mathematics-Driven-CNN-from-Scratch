# Building a Custom CNN from Scratch for MNIST Classification: A Mathematical Exploration Without High-Level Libraries

This repository demonstrates how to build a Convolutional Neural Network (CNN) from scratch, using only Python (no deep learning libraries). This project is designed to the classification of MNIST dataset and focuses on understanding and implementing the core mathematical operations behind CNNs.

## Project Overview

The goal of this project is to classify MNIST images using a custom-built CNN, created without any high-level libraries like TensorFlow or PyTorch. Every component of the network is implemented from scratch, providing a hands-on approach to understanding CNNs and their underlying math.

## Key Features

- **Data Preprocessing & Augmentation**:
  - Normalizes image pixel values for better training.
  - Augments data with random rotations and shifts to improve generalization.
  
- **CNN Layers**:
  - Basic CNN layers implemented from scratch:
    - **Convolution**: For learning image features.
    - **ReLU Activation**: Adds non-linearity.
    - **Batch Normalization**: Normalizes data to stabilize training.
    - **Max Pooling**: Reduces data dimensions, focusing on essential features.
    - **Fully Connected (Dense) Layer with Softmax**: Produces final class probabilities.

- **Training & Evaluation**:
  - Mini-batch gradient descent to update weights and biases.
  - Evaluates accuracy on the test set after each training epoch.

## CNN Architecture

The CNN follows a basic structure:

1. **Convolution Layer**: Extracts features from the image by sliding small filters across it.
2. **Batch Normalization**: Stabilizes learning by normalizing data after each batch.
3. **ReLU Activation**: Keeps values positive, introducing non-linearity to the model.
4. **Max Pooling**: Reduces spatial size, making computation more efficient.
5. **Fully Connected Layer with Softmax**: Flattens output to make predictions across classes.

### Key Math Concepts

Each CNN component is carefully implemented based on these core mathematical concepts:

- **Convolution**: Applies filters over the image to learn features like edges and textures.
- **Pooling**: Reduces dimensions by selecting the maximum value within a small window.
- **ReLU Activation**: Keeps only positive values, which speeds up learning.
- **Batch Normalization**: Normalizes layer outputs for more stable training.
- **Fully Connected Layer with Softmax**: Flattens data for classification; Softmax converts scores into probabilities for each digit.

## Code Structure

- `data_preprocessing.py`: Functions for loading, normalizing, and augmenting data.
- `cnn_layers.py`: Core CNN layer functions, including convolution, pooling, and activation functions.
- `training.py`: Training function that performs gradient updates and evaluates model accuracy.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/custom-cnn-mnist.git
   cd custom-cnn-mnist
   ```

2. Run the training script:
   ```bash
   python training.py
   ```

## Results

After training, the model will show accuracy on test data, with loss and accuracy plotted to visualize training progress.

## Contact

- Emaail: [Akhila Raveendran P M](raveendranakhila629@gmail.com)
-LinkedIn:[Akhila Raveendran P M](https://www.linkedin.com/in/akhila-raveendran-pm/)

---

