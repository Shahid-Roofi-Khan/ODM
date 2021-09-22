# -------------------------------------------------- Shahid - CPP SharedLib Import - Start

import cppyy
cppyy.include("./cpp/booster.h")
cppyy.load_library("booster")
from cppyy.gbl import Booster


# -------------------------------------------------- Shahid - CPP SharedLib import - End

def func1(mystr):
    print('my_function works.')
    print('Message: ' + mystr)
    # ----------------------------- CPP Invocation
    f = Booster()
    f.func()
    # ----------------------------- CPP Invocation End