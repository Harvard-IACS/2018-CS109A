x = np.linspace(-5.0, 5.0, 500) # input points
print(x[:5])
plt.plot(x, sigmoid(x), label='sigmoid')
plt.plot(x, np.tanh(x), label='tanh')
plt.legend()
