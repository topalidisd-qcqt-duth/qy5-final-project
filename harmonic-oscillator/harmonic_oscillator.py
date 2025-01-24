import numpy as np
from numpy.polynomial.hermite import Hermite
from scipy.integrate import quad
import math


m = 1  
h = 1  
a_0 = 1 


def psi_x(x,n, ω):
    return 1/np.sqrt(2**n*math.factorial(n)) * ( (m*ω)/(np.pi*h))**(1/4) * Hn(n,np.sqrt((m*ω)/h)*x) * np.exp((-m*ω*x**2)/(2*h))

def psi_p(p,n, ω):
    return 1/np.sqrt(2**n*math.factorial(n)) * ( 1/(np.pi*m*ω*h))**(1/4) * Hn(n,(1/np.sqrt(m*ω*h))*p) * np.exp((-p**2)/(2*m*ω*h))

def Hn(n, x):
    coefficients = np.zeros(n+1)
    coefficients[n] = 1
    return Hermite(coefficients)(x)

def integrand1(x,n,a):
    return np.log(Hn(n,a*x)**2)*Hn(n,a*x)**2*np.exp(-a**2*x**2)

def integrand2(x,n,a):
    return x**2 * Hn(n,a*x)**2 *np.exp(-a**2*x**2)

def entropy_x(n,ω):
    a = np.sqrt((m*ω)/h)
    integrand1_result, error = quad(integrand1, 0, np.inf, args=(n,a,), limit=100)   
    integrand2_result, error = quad(integrand2, -np.inf, np.inf, args=(n,a,), limit=100)   
        

    return -np.log( (a_0*a)/(2**n*math.factorial(n)*np.sqrt(np.pi))) - a/(2**n*math.factorial(n)*np.sqrt(np.pi)) * (2*integrand1_result - a**2*integrand2_result)

def entropy_p(n,ω):
    b = 1/np.sqrt(m*ω*h)
    integrand1_result, error = quad(integrand1, 0, np.inf, args=(n,b,), limit=100)   
    integrand2_result, error = quad(integrand2, -np.inf, np.inf, args=(n,b,), limit=100)   
        

    return -np.log( (h*b)/(a_0*2**n*math.factorial(n)*np.sqrt(np.pi))) - b/(2**n*math.factorial(n)*np.sqrt(np.pi)) * (2*integrand1_result - b**2*integrand2_result)

