#!/usr/bin/env python3
# by lgarciaorozco6@gmail.com Dui
# License GNU/GPL 

# Simple quiz

# def validar(s:str):
#     if 'verdadero' in a.lower() or 'falso' in a.lower(): return True
#     else: return False


b = 0
while b == 0:
    a = input('¿El sol y la luna tinen el mismo radio aparante?\nFalso/Verdadero\n>')

    if 'verdadero' in a.lower(): print('Correcto'); b += 1
    elif 'falso' in a.lower(): print('Incorrecto\nVuelve a intentarlo')
    else: print('Vuelve a intentarlo')