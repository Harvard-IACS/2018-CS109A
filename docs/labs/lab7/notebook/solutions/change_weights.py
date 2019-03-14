x = np.linspace(-5.0, 5.0, 500) # input points
f = np.exp(-x*x) # data

w = 1.5
b = -2.0

h = sigmoid(affine(x, w, b))
