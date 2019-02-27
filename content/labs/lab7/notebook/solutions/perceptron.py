w = -2.5 # weight
b = 1.0 # bias

# Perceptron output
z = affine(x, w, b) # Affine transformation
h = sigmoid(z) # Sigmoid activation
