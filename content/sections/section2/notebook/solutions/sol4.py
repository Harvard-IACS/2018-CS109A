#Filter out by First N Rows
n = 25
display(states.head(n))

#Select by Index, rows 5 to 10.
display(states.iloc[5:10,:])

#Select by List of Indices below
row_list = np.arange(1,25,2)
print(row_list)
display(states.iloc[row_list,:])
