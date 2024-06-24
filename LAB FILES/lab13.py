# Description: This program trains a neural network on the MNIST dataset using different activation
# functions and plots the validation accuracy for each activation function.
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

# Load and preprocess the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28*28).astype('float32') / 255.0
x_test = x_test.reshape(-1, 28*28).astype('float32') / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
print(x_train.shape)
print(y_test.shape)
print(x_train)
print(y_test)

# # Function to create a model with a given activation function
def create_model(activation):
    model = Sequential([
        Dense(128, input_shape=(784,), activation=activation),
        Dense(64, activation=activation),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# # # List of activation functions to test
activations = ['sigmoid', 'relu', 'tanh']
histories = {}

# # # Train and evaluate the model with each activation function
for act in activations:
    model = create_model(act)
    history = model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test), verbose=1)
    histories[act] = history

# Plot validation accuracy for each activation function
for act, history in histories.items():
    plt.plot(history.history['val_accuracy'], label=f'{act} val_accuracy')

# Plot validation loss for each activation function
for act, history in histories.items():
    plt.plot(history.history['val_loss'], label=f'{act} val_loss')

plt.title('Validation Accuracy for Different Activation Functions')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

plt.title('Validation Loss for Different Activation Functions')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
