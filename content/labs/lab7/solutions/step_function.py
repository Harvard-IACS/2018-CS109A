def full_sigmoid(x: float, a=float, c=float) -> float :
    """The sigmoid function with width `a` and threshold `c` 
    """
    return (1/(1 + np.exp(-2*(x-c)/a))) # we omit the 2 in -2(x-c)/a

def gen_step_data(my_func: np.ufunc, n: int, a=1., c=0.) -> pd.DataFrame:  
    # x values range from -xmax to +xmax+2*c
    xmax = 5
    data_list = []    
    for i in range(n):
        x = np.random.uniform(-xmax,xmax+2*c)
        y = my_func(x, a, c)
        data_list.append((x, 
                          y))
    return pd.DataFrame(data_list, columns=['x','y'])

# generate 100 simple step points with the sigmoid function 
# set parameters threshold c and width a - change a to see the change in `curvature`
a = 0.1
c = 2
step_df = gen_step_data(full_sigmoid, 100, a, c)
step_df.head(5)
