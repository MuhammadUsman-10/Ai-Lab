# Task a,b,c
import numpy as np
# Define input and weight
p = np.array([1, 2, 3, 4])
w = 0.1
n = w * p

# Define activation functions
def purelin(n):
    return n
def hardlim(n):
    return 1 if n >= 0 else 0
def logsig(n):
    return 1 / (1 + np.exp(-n))
# Calculate outputs
a1 = purelin(n)
a2 = np.array([hardlim(x) for x in n])
a3 = logsig(n)
print("With 4 Elements:")
print(f"Linear: {a1}")
print(f"Hard-limit: {a2}")
print(f"Sigmoid: {a3}")


#Deliverable Part ***** XOR Implementation *****
import numpy as np

# Sigmoid activation function
def sigmoid(n):
    return 1 / (1 + np.exp(-n))

# Derivative of the sigmoid function
def sigmoid_derivative(n):
    return n * (1 - n)

# XOR dataset
input_set = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
output_set = np.array([[0], [1], [1], [0]])

# Seed for reproducibility
np.random.seed(42)

# Initialize weights and biases
input_layer_neurons = 2
hidden_layer_neurons = 2
output_neurons = 1

# Weights and biases
wh = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
bh = np.random.uniform(size=(1, hidden_layer_neurons))
wout = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

# Training parameters
epochs = 10000
learning_rate = 0.1

# Training the neural network
for epoch in range(epochs):
    # Forward Propagation
    hidden_layer_input = np.dot(input_set, wh) + bh
    hidden_layer_activation = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_activation, wout) + bout
    predicted_output = sigmoid(output_layer_input)
    
    # Backpropagation
    error = output_set - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)
    
    error_hidden_layer = d_predicted_output.dot(wout.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_activation)
    
    # Updating Weights and Biases
    wout += hidden_layer_activation.T.dot(d_predicted_output) * learning_rate
    bout += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    wh += input_set.T.dot(d_hidden_layer) * learning_rate
    bh += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

# Testing the neural network
hidden_layer_input = np.dot(input_set, wh) + bh
hidden_layer_activation = sigmoid(hidden_layer_input)

output_layer_input = np.dot(hidden_layer_activation, wout) + bout
predicted_output = sigmoid(output_layer_input)

print("XOR Predicted Output by Neural Network: \n", predicted_output)
print("\nXOR Actual Output: \n", output_set)