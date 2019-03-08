# Add noise
bikeshare['temp'] = bikeshare['temp']+np.random.normal(loc=0, scale=0.0001, size=bikeshare.shape[0])
