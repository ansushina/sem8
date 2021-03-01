  
from numpy.random import rayleigh
from scipy.stats import weibull_min
import random
import numpy as np
import math

class RayleighDistribution:
    def __init__(self, sigma: float):
        self.sigma = sigma

    def generate(self):
        return rayleigh(self.sigma)

class WeibullDistribution:
    def __init__(self, k: float,lambd: float):
        self.k = k
        self.lam = lambd

    def generate(self):
        return weibull_min.rvs(self.k, loc=0, scale=self.lam)
    