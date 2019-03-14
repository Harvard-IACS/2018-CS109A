#Select by Name : Filter out only '1930','1940','1950','1960' columns.
display(states[['1930','1940','1950','1960']].head())

#Select by Index : Filter out only first 3 columns
display(states.iloc[:,0:3].head())

#Select by List : Filter out following list of columns
columns_list = ['1920','1840']
display(states[columns_list].head())
