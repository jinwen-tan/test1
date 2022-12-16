import numpy as np #import numpy module 

#function to return the calculated degree celcius to farenheit convertion algorithm
def calc_degree_to_faren (val_degree):
    return val_degree * 1.8 + 32 

#random input 
val_degree = np.random.rand(1,5)  #generate random number with 1 row and 5 colums 
degree_to_faren = calc_degree_to_faren(val_degree) #function call to calculate the convertion 

#ouput
print("Degree to Ferenheit convertion = ", degree_to_faren) 