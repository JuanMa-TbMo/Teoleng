# -*- coding: utf-8 -*-
import re
import sys
import programa1
import datetime

def programa2(RutaFactura):
    texto = programa1.programa1(RutaFactura)
    aniomesdia=re.search(r'FECHA:(\d{4}-\d{2}-\d{2})', texto)
    diamesanio=re.search(r'FECHA:(\d{2}-\d{2}-\d{4})', texto)
    if aniomesdia:
        anio,mes,dia=aniomesdia.groups()
        fecha_obj = datetime(int(anio), int(mes), int(dia)).date()
        fecha_encontrada = fecha_obj.strftime("%Y-%m-%d")
    elif diamesanio:
        dia,mes,anio=diamesanio.groups()
        fecha_obj = datetime(int(anio), int(mes), int(dia)).date()
        fecha_encontrada = fecha_obj.strftime("%Y-%m-%d")
    
    
    
    monto=re.search(r'DÉBITO BANCARIO\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2})?', texto)
    '''
    SU CÓDIGO
    
    NOTA: El formato de la fecha debe ser AAAA-MM-DD 
    '''
    
    fecha =  fecha_encontrada     
    return fecha, monto
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    fecha,monto = programa2(entrada)      # ejecutar 
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
