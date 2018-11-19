import numpy as np
import matplotlib.pyplot as plt

def f(x):
    
    return 1/(16*(x**2) + 1)

#Using 21 'equally spaced nodes' on the interval [-1,1], 
# construct the interpolating polynomial p of degree 20 for the
#function defined above, using Newton divided differences.

nodes = np.linspace(-1,1,num=21) #nodes to use for interpolant
f_val_nodes = f(nodes)
poly_order = 20

#defining the Newton divided differences function to calculate the divided differences:

def Newton_Divided_differences(nodes, f_val_nodes, poly_order):
    
    Divided_differences_mat = np.zeros(shape = (len(nodes), poly_order+1))
    F = []
    #populating the matrix with f_val_nodes
    for k in range(0,1):
        
        for l in range(0, Divided_differences_mat.shape[0]):
            
            Divided_differences_mat[l,k] = f_val_nodes[l]
         
    #populating the matrix with divided differences    
    for i in range(1, len(nodes)):
        
        for j in range(1,i+1):
            
            Divided_differences_mat[i,j] = (Divided_differences_mat[i,j-1] - Divided_differences_mat[i-1,j-1])/(nodes[i] - nodes[i-j])

    #extracting the divided differences needed to construct the interpolant   
    for n in range(0, poly_order+1 ):
        
        F.append(Divided_differences_mat[n,n])
    
    return F

F_diffs = Newton_Divided_differences(nodes, f_val_nodes, poly_order = 20)

#Defining the Interpolant_Poly function which returns the polynomial y values evaluated
#for a given set of x values.

def Interpolant_Poly(F_diffs, nodes, x_points, poly_order):
    
    #(x-xi)'s:
    poly_points = []
    
    for j in range(0, len(x_points)):
        
        product_of_x_factors = 1
        list_of_factor_products = []
        
        for i in range(0, poly_order):
        
            factor = (x_points[j]-nodes[i])
            product_of_x_factors = factor*product_of_x_factors
            list_of_factor_products.append(product_of_x_factors) #[(x-x0), (x-x0)(x-x1), ..., (x-x0)(x-x1)..(x-x_n-1)]
    
        
        poly_points.append(F_diffs[0] + np.sum(np.array(F_diffs[1:])*np.array(list_of_factor_products)))
    
    return poly_points

x_values = np.arange(-1,1,0.01) # x values to use in plot of interpolant vs f

plt.plot(x_values, f(x_values), label = "f(x)")
plt.plot(x_values, Interpolant_Poly(F_diffs, nodes, x_values, poly_order= 20) , label = "Interpolant")
plt.title("Interpolanting polynomial of degree 20 vs f(x) using equally spaced nodes")
plt.ylim((-1,1.5))
plt.legend()
plt.show()

### -------------
#Using 21 'chebyshev nodes' on the interval [-1,1], 
# construct the interpolating polynomial p of degree 20 for the
#function defined above, using Newton divided differences.
# chebyshev nodes mitigate the "runge phenomenon" 
# "runge phenomenon" -> high order polynomials performing poorly at end of intervals for evenly spaced nodes

cheby_nodes = []
for k in range(1, poly_order+2):
    
    cheby_nodes.append(np.cos(((2*k -1)/(2*poly_order))*np.pi))

F_diffs_cheby = Newton_Divided_differences(cheby_nodes, f(np.array(cheby_nodes)), poly_order = 20)

x_values = np.arange(-1,1,0.01)
plt.plot(x_values, f(x_values), label = "f(x)")
plt.plot(x_values, Interpolant_Poly(F_diffs, nodes, x_values, poly_order= 20) , label = "Equal-spaced node Interpolant")
plt.plot(x_values, Interpolant_Poly(F_diffs_cheby, cheby_nodes, x_values, poly_order= 20) , label = "Chebyshev node Interpolant")
plt.ylim((-1,1.5))
plt.legend()
plt.show()