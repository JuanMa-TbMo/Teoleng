# -*- coding: utf-8 -*-
import re
import sys
from programa2 import programa2 as obtener_fecha_monto
from programa4 import programa4 as leer_xml

def programa5(RutaPdf,RutaXML):
    resultado = False

    # Explicación del regex:
    # Línea 1: busco el texto "<BanTeng:Movimiento" y un espacio en blanco ("\s")
    # Línea 2: busco el texto 'TipoMov="{C_o_D}"', y en {C_o_D} la letra "C" o la "D", seguido de un espacio en blanco
    # Línea 3: busco el texto 'Importe="{monto}"', y en {monto} el monto leído de la factura, seguido de un espacio en blanco
    # Línea 4: busco el texto 'Fecha="{fecha}"', y en {fecha} la fecha leída de la factura
    # Línea 5: si el XML está bien formado, esta línea es innecesaria. La puse por las dudas que la entrada <BanTeng:Movimiento ... /> no esté bien formada.
    #          Busca que no haya ningún ("^") salto de línea (newline: "\n") o un carriage return ("\r") hasta llegar a un "/>".

    '''
    SU CÓDIGO
    '''

    fecha, monto = obtener_fecha_monto(RutaPdf)
    xml = leer_xml(RutaXML)

    patron = (
        r"<BanTeng:Movimiento\s"
        + r'TipoMov="[CD]"\s'
        + rf'Importe="{monto}"\s'
        + rf'Fecha="{fecha}"'
        + r"[^\r\n]*/>"
    )

    resultado = re.search(patron, xml) is not None

    if resultado:
        return(True)
    else:
        return(False)

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa5(entrada_pdf,entrada_xml)      # ejecutar 
    if (ret):
        ret = "Encontrado"
    else:
        ret = "No encontrado"
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
