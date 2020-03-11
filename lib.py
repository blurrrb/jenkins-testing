def power(x, y, p) : 
    res = 1 
    x = x % p  
  
    while (y > 0) : 
        if ((y & 1) == 1) : 
            res = (res * x) % p  
        y = y >> 1 
        x = (x * x) % p 
          
    return res

def mod_inverse(a, m): 
    a = a % m
    for x in range(1, m): 
        if ((a * x) % m == 1): 
            return x 
    return 1