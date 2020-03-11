from lib import mod_inverse, power
from sys import exit

def power_test():
    x = 2
    y = 2
    m = 3

    fn_res = power(x, y, m)
    actual_result = (x**y) % m
    if fn_res != actual_result:
        print('fast modular exponentiation failed')
        return False
    else:
        print('fast modeular exponentiation passed')
        return True

def modinv_test():
    a = 3
    m = 29

    if (a * mod_inverse(a, m)) % m != 1:
        print('fast mod inverse failed')
        return False
    else:
        print('fast mod inverse passed')
        return True


def main():
    res = True
    tests = [power_test, modinv_test]

    for test in tests:
        res = res & test()
    
    if res:
        print('all tests successful')
        exit(0)
    else:
        print('some tests failed')
        exit(1)

if __name__ == "__main__":
    main()