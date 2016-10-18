import sys
sys.path.append("../..")
from local import *

import numpy as np
import pandas as pd
import json

from r1basis import *

L = 1
ene = 0.5

def zs_et_from_num(num, z0=0.01, z1=30.0):
    return np.array([z0 * (z1/z0)**(n*1.0/(num-1)) for n in range(num)])

def calc():
    ## optimized basis set
    zs = 

    ## build basis functions
    zs = (zs_et_from_num(15, 0.01, 30.0) +
          get_opt_zeta())
    b = GTOs()
    b.add(2, zs)
    b.setup()
    
    ## velocity driven term
    driv = LC_STOs()
    driv.add(2.0, 1, 1.0)
    
    ## matrix and vector
    lmat = ( b.calc_rm_mat(0)  * ene
            + b.calc_d2_mat()* 0.5
            + b.calc_rm_mat(-2)* (-0.5*(-L*(L+1)))
            + b.calc_rm_mat(-1))
    mvec = ss.calc_vec(driv)
    cs = solve(lmat, mvec)
    alpha = np.dot(cs, mvec)
    
    print alpha

calc()
