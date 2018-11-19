import numpy as np

#function to integrate:
def f(x):
    return 2/(x**2 +4)

#function to apply the composite trapezoidal integration method to the above function
def Composite_Trapezoidal(start,end,num_points):
    
    z = np.linspace(start,end,num_points) 
    n = num_points -1 #n equally spaced subintervals 
    h = (end-start)/n
    I_approx = []  #array to store the integral values over each subinterval
    
    for i in range(0,n):
        
        I_temp = (h/2)*(f(z[i]) + f(z[i+1])) #applying the trapezoidal method over each sub-interval
        I_approx.append(I_temp)
    
    return np.array(I_approx).sum() #sum integral values over all sub-intervals 

Integral_value = Composite_Trapezoidal(0,2,7)
print("Integral evaluated using Composite_Trapezoidal function:", Integral_value)

#correction check - using scipy library:
from scipy.integrate import trapz
x = np.linspace(0,2,7)
print("Integral evaluated using scipy's trapz function:", trapz(f(x),x))