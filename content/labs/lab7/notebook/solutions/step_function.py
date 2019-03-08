def full_sigmoid(x: float, a=float, c=float) -> float :
    """The sigmoid function with width `a` and threshold `c` 
    """
    return (1/(1 + np.exp(-2*(x-c)/a))) # we omit the 2 in -2(x-c)/a


# generate 500 simple step points with the sigmoid function 
# set parameters threshold c and width a - change a to see the change in `curvature`
a = 0.1
c = 2

x = np.linspace(-5.0, 5.0, 500) # input points
f = full_sigmoid(x, a, c) # data

plt.plot(x, f,  lw=4, label=r'True function')
