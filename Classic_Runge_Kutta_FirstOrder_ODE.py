import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#ODE defined as y' = f(t,y)
def f(t, y):
    return y - t**2 +1

def Classic_Runge_Kutta(start, end, init_condition, num_points):
    
    h = (end-start)/num_points
    t = start
    w = init_condition
    approximations = [init_condition]
    nodes = [start]
    
    #creating the four intermediate stages of RK4 Method
    for i in range(1,num_points+1):
        K1 = h*f(t,w)
        K2 = h*f(t + 0.5*h, w + 0.5*K1)
        K3 = h*f(t + 0.5*h, w + 0.5*K2)
        K4 = h*f(t + h, w + K3)
        
        w = w + (1/6)*(K1+2*K2+2*K3+K4) #y approximation at each node
        t = start + i*h
        
        approximations.append(w)
        nodes.append(t)
        
    return approximations,nodes

approx, t_nodes = Classic_Runge_Kutta(0,2,0.5,10)

#printing out the approximate solutions at the mesh points in a dataframe
df = pd.DataFrame({"mesh points": t_nodes, "y approximations": approx})
print(df)

#plotting the solutions
plt.scatter(t_nodes, approx, marker = "o")
plt.title("Solution to first order ODE")
plt.xlabel("mesh points")
plt.show()