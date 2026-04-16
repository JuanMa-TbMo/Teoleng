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
    paginas = len(reader.pages)
    while paginas > 0: #cambiar por for
        pagina = reader.pages[paginas-1]
        textoNeto += pagina.extract_text()
        paginas -= 1
    text=textoNeto
    
    
    return text


if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    ret = programa1(entrada)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
