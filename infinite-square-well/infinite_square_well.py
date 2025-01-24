import numpy as np
from scipy.integrate import quad 

h = 1     
a_0 = 1


def b(n,L):
    return (n*np.pi)/(2*L)

def c(p):
    return p/h

def psi_x_odd(x,n,L):
    return (1/np.sqrt(L)) * np.cos((n*np.pi*x)/L)
    
def psi_x_even(x,n,L):
    return (1/np.sqrt(L)) * np.sin((n*np.pi*x)/L)

def psi_p_odd(p,n,L):
    return ( (2*b(n,L)*(-1)**((n+1)/2))/(np.sqrt(2*np.pi*h*L)*(c(p)**2 - b(n,L)**2) ) ) * np.cos(c(p)*L)

def psi_p_even(p,n,L):
    return ( (2*b(n,L)*(-1)**((n+2)/2))/(np.sqrt(2*np.pi*h*L)*(c(p)**2 - b(n,L)**2) ) ) * np.sin(c(p)*L)
    
def entropy_x(x,n,L):
    rho=None
    if n%2==0:
        rho =  psi_x_even(x,n,L)**2
    else:
        rho =  psi_x_odd(x,n,L)**2
    
    return -rho*np.log(a_0 * rho) 

def entropy_p(p,n,L):
    gamma=None
    if n%2==0:
        gamma =  psi_p_even(p,n,L)**2
    else:
        gamma =  psi_p_odd(p,n,L)**2
    
    return -gamma*np.log((h/a_0) * gamma)

def calc_entropy_x(n, L):
    
    a = -L
    b = L
    c = 1

    if n%2==0:
        a=0
        c=2

    result, error = quad(entropy_x, a, b, args=(n,L,), limit=1000)    
    return c*result

def calc_entropy_p(n, L):
    
    a = -np.inf
    b = np.inf
    c = 1

    result, error = quad(entropy_p, a, b, args=(n,L,), limit=1000)   

    return c*result

s_x_ground_state = round(calc_entropy_x(1,0.05), 4)
s_p_ground_state = round(calc_entropy_p(1,0.05), 4)
s_t_ground_state = s_x_ground_state + s_p_ground_state
