# -*- coding: utf-8 -*-
import re
import sys
import pypdf 


def programa1(RutaPdf):
    '''
    SU CÓDIGO
    '''
    textoNeto = ""
    reader = pypdf.PdfReader(RutaPdf)
    for pagina in reader.pages:
        textoNeto += pagina.extract_text()

    text=textoNeto
    
    
    return text


if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa1(entrada)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
