import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import math
from scipy.integrate import quad

def driver():

#  function you want to approximate
    f = lambda x: math.exp(x) # 1 / (1 + (x**2)) 

# Interval of interest    
    a = -1
    b = 1
# weight function    
    w = lambda x: 1

# order of approximation
    n = 2

#  Number of points you want to sample in [a,b]
    N = 1000
    xeval = np.linspace(a,b,N+1)
    pval = np.zeros(N+1)

    for kk in range(N+1):
      pval[kk] = eval_legendre_expansion(f,a,b,w,n,xeval[kk])
      
    ''' create vector with exact values'''
    fex = np.zeros(N+1)
    for kk in range(N+1):
        fex[kk] = f(xeval[kk])
        
    plt.figure()    
    plt.plot(xeval,fex,'ro-', label= 'f(x)')
    plt.plot(xeval,pval,'bs--',label= 'Expansion') 
    plt.legend()
    plt.show()    
    
    err_l = abs(pval-fex)
    plt.semilogy(xeval,err_l,'ro--',label='error')
    plt.legend()
    plt.show()
    
      
    

def eval_legendre_expansion(f,a,b,w,n,xval): 

#   This subroutine evaluates the Legendre expansion

#  Evaluate all the Legendre polynomials at x that are needed
# by calling your code from prelab 
  p = eval_legendre(n,xval)
  
  # initialize the sum to 0 
  pval = 0.0    
  for j in range(0,n+1):
      # make a function handle for evaluating phi_j(x)
      phi_j = lambda x: p[j]
      # make a function handle for evaluating phi_j^2(x)*w(x)
      phi_j_sq = lambda x: phi_j(xval)**2
      # use the quad function from scipy to evaluate normalizations
      norm_fac = lambda x: phi_j_sq(xval) * w(xval) # ,err = ...
      norm_fac_val = quad(norm_fac,a,b)[0]
      # make a function handle for phi_j(x)*f(x)*w(x)/norm_fac
      func_j = lambda x: phi_j(xval) * f(xval) * w(xval) / norm_fac_val # lambda x: ...
      # use the quad function from scipy to evaluate coeffs
      aj = quad(func_j,a,b)[0]  # ,err = ...
      # accumulate into pval
      pval = pval + aj*p[j]
    
  return pval

def eval_legendre(n,x):
    
    p = np.zeros(n+1)
    p[0] = 1
    p[1] = x

    for phi in range(2,n+1):
        p[phi] = (1 / (phi + 1))*(((2*phi) + 1)*x*p[phi-1] - phi*p[phi-2])

    print(p)
    return p
        
driver()   