# number of hidden nodes
H = 40
# input dimension
input_dim = 1

# create sequential multi-layer perceptron
model2 = models.Sequential()
# layer 0
model2.add(layers.Dense(H, input_dim=input_dim, 
                kernel_initializer='normal', 
                activation='tanh')) 
# layer 1
model2.add(layers.Dense(H,
                kernel_initializer='normal', 
                activation='tanh')) 
# layer 2
model2.add(layers.Dense(H,
                kernel_initializer='normal', 
                activation='tanh')) 
# layer 3
model2.add(layers.Dense(H,  
                kernel_initializer='normal', 
                activation='tanh')) 
# layer 4
model2.add(layers.Dense(H,  
                kernel_initializer='normal', 
                activation='tanh')) 
# layer 5
model2.add(layers.Dense(H,  
                kernel_initializer='normal', 
                activation='tanh')) 
# layer 6
model2.add(layers.Dense(1, kernel_initializer='normal', 
                activation='linear')) 

# configure the model
model2.compile(loss='mean_squared_error', optimizer='adam')
