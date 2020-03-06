# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

def l100kmtompg(litres):
    gallons=litres/3.785411784
    miles=100*1000/1609.344
    return miles/gallons
def mpgtol100km(miles):
    km100=miles*1609.344/1000/100
    litres=3.785411784
    return litres/km100
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
"""
Resultado esperado:
60.31143162393162 31.36194444444444 23.52145833333333 
3.9007393587617467 7.490910297239916 10.009131205673757

"""