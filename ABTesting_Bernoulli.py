'''

A/B Testing

Bernoulli Distribtion

N: people who saw the ads
n: people who saw and clicked the ads
p: mean
sigma: standard deviation

it is ok to not use t-test (should have because standard deviation is unknown)

'''
import math


def estimated_parameters(N,n):
    
    p = n/N
    sigma = math.sqrt(p*(1-p)/N)
    return p, sigma

'''
hypothesis: no difference in effectiveness between ads A and ads B

mean p_B - p_A
standar deviation sqrt(sigma_A**2 +sigma_B**2)

'''

def a_b_test_statistic(N_A,n_A,N_B,n_B):
    
    p_A, sigma_A = estimated_parameters(N_A,n_A)
    
    p_B, sigma_B = estimated_parameters(N_B,N_B)
    
    return (p_B - p_A)/math.sqrt(sigma_A**2+sigma_B**2)

'''
z = a_b_test_statistic(N_A,n_A,N_B,n_B)

then check if we can accept/reject null hypothesis

'''
