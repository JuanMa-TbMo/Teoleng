# -*- coding: utf-8 -*-
import re
import sys
import programa1

def programa3(RutaFactura):
    
    '''
    SU CÓDIGO
    
    
    '''
    
    texto = programa1.programa1(RutaFactura)

    patron = r'posible patron jeje'

    

    res=f"Cant: 10 |Desc: PRUEBA | 10,10 c/u |Total: 101\n"
    


    
    return res

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)    
 
    ret = programa3(entrada)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
