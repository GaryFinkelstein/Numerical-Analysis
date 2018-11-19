import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#fourh order Classic Runge Kuttta method to solve the following 1st order system using time step of h =0.05s and up t = 5s:
#dN1/dt = -N1   ; N1(0) = 100
#dn2/dt = N1-N2 ; N2(0) = 0

#function used by the intermediate stages K1, K2, K3,K4
def f(j,t,y_vec):
    
    if j ==1:
        return -y_vec[0]
    elif j ==2:
        return y_vec[0] - y_vec[1]

def Classic_Runge_Kutta_Systems(start, end, num_equations, init_conditions_vec, num_points):
    
    h = (end-start)/num_points
    t = start
    w = init_conditions_vec
    K1 = np.zeros( num_equations)
    K2 = np.zeros( num_equations)
    K3 = np.zeros( num_equations)
    K4 = np.zeros( num_equations)
    t_nodes = [start]
    approx_solutions_vec = [np.array(init_conditions_vec)]
   
    #Updating intermediate stages and determining an approximation at the n'th node
    for i in range(1,num_points+1):
        
        for j in range(0, num_equations):
            
            K1[j] = h*f(j+1,t,w)
        K1 = np.array(K1)
            
            
        for j in range(0, num_equations):
            
            K2[j] = h*f(j+1,t+0.5*h,w + 0.5*K1)
        K2 = np.array(K2)
            
            
        for j in range(0, num_equations):
            
            K3[j] = h*f(j+1,t+0.5*h,w + 0.5*K2)
        K3 = np.array(K3)
            
            
        for j in range(0, num_equations):
            
            K4[j] = h*f(j+1,t+h,w +K3)
        K4 = np.array(K4)
            
            
        for j in range(0, num_equations):
            
            w[j] = w[j] + (1/6)*(K1[j]+2*K2[j]+2*K3[j]+K4[j])
        
        t = start + i*h
        
        approx_solutions_vec.append(np.array(w))
        t_nodes.append(t)
        
    return approx_solutions_vec, t_nodes

approx_sols, t_nodes = Classic_Runge_Kutta_Systems(0,5,2,[100,0],100)

#printing out solutions in readable format (dataframe)
df = pd.DataFrame({"mesh_points": np.array(t_nodes), "[Approx.Solution N1, Approx.Solution N2]": approx_sols})
print(df)

#plotting the solutions
appr_n1 = []
appr_n2 = []
for i in range(0, len(t_nodes)):
    
    appr_n1.append(approx_sols[i][0])
    appr_n2.append(approx_sols[i][1])

plt.scatter(t_nodes,appr_n1, label = "N1", s = 5)
plt.scatter(t_nodes,appr_n2, label = "N2", s = 5)
plt.title("Plot of approximate solutions to the coupled system of ODES")
plt.legend()
plt.show()