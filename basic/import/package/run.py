import sys

import m1

# import pkg.m2 as m2

sys.path.append(r'D:\github\python\basic\import\package\pkg')
import pkg.m2

print(__name__)
from pkg.subpkg import f2, f4

if __name__ == '__main__':
    f2()
    f4()
