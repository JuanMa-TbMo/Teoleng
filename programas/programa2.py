# -*- coding: utf-8 -*-
import re
import sys
import programa1
import datetime

def programa2(RutaFactura):
    texto = programa1.programa1(RutaFactura)
    aniomesdia=re.search(r'FECHA:\s*(\d{4})[-/](\d{2})[-/](\d{2})', texto) #digitos, guion o barra, digitos, guion o barra, digitos
    diamesanio=re.search(r'FECHA:\s*(\d{2})[-/](\d{2})[-/](\d{4})', texto)

    fecha_encontrada = "None"
    monto_encontrado = "None"
    if aniomesdia:
        anio,mes,dia=aniomesdia.groups()
        try:
            fecha_obj = datetime.datetime(int(anio), int(mes), int(dia)).date()
            fecha_encontrada = fecha_obj.strftime("%Y-%m-%d")
        except ValueError:#eplota en caso de fecha invalida, por ejemplo 2023-02-31
            fecha_encontrada = "None"
    elif diamesanio:
        dia,mes,anio=diamesanio.groups()
        try:
            fecha_obj = datetime.datetime(int(anio), int(mes), int(dia)).date()
            fecha_encontrada = fecha_obj.strftime("%Y-%m-%d")
        except ValueError:
            fecha_encontrada = "None"

    monto_encontrado=re.search(r'DÉBITO\s+BANCARIO\s*(\d+(?:[,\.]\d+)?)', texto)
   
    if monto_encontrado:
        monto_encontrado = monto_encontrado.group(1)
     
        monto_encontrado = monto_encontrado.replace('.', ',') 
     
    

    '''
    SU CÓDIGO
    
    NOTA: El formato de la fecha debe ser AAAA-MM-DD 
    '''
    monto= monto_encontrado

    fecha =  fecha_encontrada     
    return fecha,monto
  

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    fecha,monto = programa2(entrada)      # ejecutar 
    ret =f"Fecha: {fecha} | Monto: {monto}"
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
