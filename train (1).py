# -*- coding: utf-8 -*-
"""train.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ubl8oH3KV0bc7ucqsD7ZJveS7vvZztZa
"""

import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score


def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))  # For numerical stability
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)

def cross_entropy_loss(y_true, y_pred):
    return -np.mean(np.sum(y_true * np.log(y_pred + 1e-10), axis=1))  # Adding small value to avoid log(0)

def compute_gradients(x_input, y_batch, conv_kernel, conv_bias, fc_weights, fc_bias):
    # Forward pass through CNN layers
    conv_out = conv2d(x_input, conv_kernel) + conv_bias
    conv_out = batch_norm(conv_out)
    conv_out = relu(conv_out)
    pool_out = max_pool2d(conv_out, pool_size=2)
    flattened_input = flatten(pool_out)

    # Forward pass through fully connected layer
    output = np.dot(flattened_input, fc_weights) + fc_bias
    y_pred = softmax(output)

    # Backward pass
    dL_dout = y_pred - y_batch  # Derivative of the loss with respect to the output
    dL_dfc_weights = np.dot(flattened_input.T, dL_dout)  # Gradient for fully connected weights
    dL_dfc_bias = np.sum(dL_dout, axis=0)  # Gradient for fully connected biases

    # Backpropagate through the layers (implement the actual gradients for the conv layers if needed)

    return dL_dfc_weights, dL_dfc_bias, y_pred, conv_out, flattened_input

# Adjust the flattened size calculation for both training and testing
def get_flattened_size(x_input, conv_kernel, pool_size=2):
    conv_out = conv2d(x_input, conv_kernel) + conv_bias
    conv_out = batch_norm(conv_out)
    conv_out = relu(conv_out)
    pool_out = max_pool2d(conv_out, pool_size)
    return np.prod(pool_out.shape[1:])  # Compute flattened size

# Training the model using mini-batch gradient descent
def train_model(x_train, y_train, x_test, y_test, conv_kernel, conv_bias, fc_weights, fc_bias, learning_rate, batch_size, num_epochs):
    loss_history = []
    accuracy_history = []

    # Get the flattened size for both training and test data
    flattened_size = get_flattened_size(x_train[:batch_size], conv_kernel)  # Use a batch sample to compute size
    fc_weights = np.random.randn(flattened_size, num_classes)
    fc_bias = np.random.randn(num_classes)

    # Loop through epochs
    for epoch in range(num_epochs):
        print(f"Epoch {epoch+1}/{num_epochs}")
        num_batches = len(x_train) // batch_size
        for batch_idx in range(num_batches):
            # Get the current batch
            x_batch = x_train[batch_idx * batch_size : (batch_idx + 1) * batch_size]
            y_batch = y_train[batch_idx * batch_size : (batch_idx + 1) * batch_size]

            # Compute gradients and forward pass
            dL_dfc_weights, dL_dfc_bias, y_pred, conv_out, flattened_input = compute_gradients(x_batch, y_batch, conv_kernel, conv_bias, fc_weights, fc_bias)

            # Update fully connected layer weights and biases
            fc_weights -= learning_rate * dL_dfc_weights
            fc_bias -= learning_rate * dL_dfc_bias

            # Calculate loss for the current batch
            loss = cross_entropy_loss(y_batch, y_pred)
            loss_history.append(loss)

        # Pass test data through the CNN layers (convolution, pooling) before flattening
        conv_out_test = conv2d(x_test, conv_kernel) + conv_bias
        conv_out_test = batch_norm(conv_out_test)
        conv_out_test = relu(conv_out_test)
        pool_out_test = max_pool2d(conv_out_test, pool_size=2)
        flattened_test = pool_out_test.reshape(len(x_test), -1)  # Flatten after pooling

        # Predict using the fully connected layer
        y_test_pred = np.argmax(softmax(np.dot(flattened_test, fc_weights) + fc_bias), axis=1)
        y_test_true = np.argmax(y_test, axis=1)
        accuracy = accuracy_score(y_test_true, y_test_pred)
        accuracy_history.append(accuracy)
        print(f"Test Accuracy: {accuracy*100:.2f}%")

    return loss_history, accuracy_history, fc_weights, fc_bias




# Setting the hyperparameters
batch_size = 32
learning_rate = 0.01
num_epochs = 10

# Initialize weights and biases
conv_kernel = np.random.randn(3, 3, 1, 10)  # 3x3 filter, 1 input channel, 10 output channels
conv_bias = np.random.randn(10)
fc_weights = np.random.randn(1690, num_classes)  # Flattened size should match the output of pooling
fc_bias = np.random.randn(num_classes)

# Training the model
loss_history, accuracy_history, fc_weights, fc_bias = train_model(
    x_train_augmented, y_train_onehot, x_test, y_test_onehot,
    conv_kernel, conv_bias, fc_weights, fc_bias,
    learning_rate, batch_size, num_epochs
)

# Plot loss and accuracy
plt.figure(figsize=(12, 5))

# Loss curve
plt.subplot(1, 2, 1)
plt.plot(loss_history)
plt.title('Loss Curve')
plt.xlabel('Iterations')
plt.ylabel('Loss')

# Accuracy curve
plt.subplot(1, 2, 2)
plt.plot(accuracy_history)
plt.title('Accuracy Curve')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')

plt.tight_layout()
plt.show()