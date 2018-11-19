import numpy as np

# Find roots of x**3 - 5*(x^2) -100*x + 500 -> -10, 5 and 10

#absolute value function
def f_abs(x):
    epsilon = 1*10**(-10)
    if np.absolute(x) < epsilon:
        return True
    else:
        return False

#f(x)
def f(x):
    return x**3 - 5*(x**2) -100*x + 500

#f'(x)
def f_prime(x):
    return 3*(x**2) -10*x -100

#=================================================================================
#Applying Newtons Method, Secant Method and Bisection Method to find roots of f(x):
#=================================================================================


 #Newton Raphson root finding method for starting point x and iterating N times

def NewtonsMethod(x, N):
    x_n =x
    count =0

    while (f_abs(f(x_n)) == False and f_abs(f_prime(x_n)) == False and count < N):
            
        x_n1 = x_n - f(x_n)/f_prime(x_n)
        x_n = x_n1
        count+=1
        
    return x_n

print("Newtons method:")
def print_roots_newton(start, N):

    print("Initial guess = ", start, " root = " ,NewtonsMethod(start,N))

print_roots_newton(-2,5) 
print_roots_newton(7.8,5)
print_roots_newton(25,5)
print_roots_newton(-16,5)

#--------
#Secant root finding method for starting point x and iterating N times

def Secant_Method(x, N):
    
    x0 =x
    x1 = x+0.25
    count = 0
    f0 = f(x0)
    f1 = f(x1)
    
    
        
    while (f_abs(f(x)) == False and count < N):
                
        if(np.absolute(f1-f0) > 1*10**(-10)):
            x = x1 - f1*(x1-x0)/(f1-f0)
            
            f0 = f1
            x0 = x1
            x1 = x
            f1 = f(x1)
           
        else:
            break
                    
        count+=1      
        
    return x

print("secant method:")
def print_roots_secant(start, N):
    print("Initial guess = ", start, " root = " ,Secant_Method(start,N))

print_roots_secant(-2,5) 
print_roots_secant(7.8,5)
print_roots_secant(25,5)
print_roots_secant(-16,5)

#-----
#Bisection Method

def Bisection_Method(x,N):
    count = 0
    a = x
    if f(a) < 0:
        
        b =11
    else:
        b = -11
        
    x1 = (a+b)/2
    
    while(f_abs(f(x1)) == False and count < N ):
            
            if f(x1) < 0:
                
                if f(a) <0:
                    a = x1
                elif f(b) <0:
                    b = x1
                
            elif f(x1) > 0:
                
                if f(a) > 0:
                    a = x1
                elif f(b) > 0:
                    b = x1
            
            x1 = (a+b)/2
            
            count +=1
    return x1

print("bisection method:")
def print_roots_bisection(start, N):
    
    print("Initial guess = ", start, " root = " , Bisection_Method(start,N))

print_roots_bisection(-2,5) 
print_roots_bisection(7.8,5)
print_roots_bisection(25,5)
print_roots_bisection(-16,5)