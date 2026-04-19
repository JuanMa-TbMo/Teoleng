# -*- coding: utf-8 -*-
import re
import sys
import programa1

def programa3(RutaFactura):
    
    '''
    SU CÓDIGO
    
    
    '''
    
    texto = programa1.programa1(RutaFactura)

    #Dejo la explicación del regex por si tienen alguna duda
    #(\d+) uno o más dígitos
    #\s+ uno o más espacios entre columnas
    #(.+?) el . es cualquier caracter excepto salto de línea, y el ? es para que tome lo mínimo necesario.
    #(\d+,\d{2}) uno o más dígitos seguido de una coma seguido de exactamente dos dígitos para los decimales.

    patron = r'(\d+)\s+(.+?)\s+(\d+,\d{2})\s+(\d+,\d{2})'

    items = re.findall(patron, texto)

    res = ""

    for cant, desc, unit, total in items:
        res += f"Cant: {cant} |Desc: {desc.strip()} | {unit} c/u |Total:  {total}\n"

    #res=f"Cant: 10 |Desc: PRUEBA | 10,10 c/u |Total: 101\n"
    

    return res

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)    
 
    ret = programa3(entrada)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida