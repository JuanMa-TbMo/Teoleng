# -*- coding: utf-8 -*-
import re
import sys
from programa5 import programa5 as hay_movimiento_coincidente
from programa4 import programa4 as leer_xml
from programa2 import programa2 as obtener_fecha_monto

def programa6(RutaPdf, RutaXML):
    text = leer_xml(RutaXML)
    
    if not hay_movimiento_coincidente(RutaPdf, RutaXML):
        return text

    fecha, monto = obtener_fecha_monto(RutaPdf)

    # Uso re.MULTILINE para que el simbolo ^ cambie de significado y asi me lo interprete como "el inicio de linea"
    # ^\s* significa; al inicio de la linea la cantidad de espacios que sea
    # [^>]* significa; cualquier secuencia de caracteres hasta que encuentre un >
    # El \n al final del patron es para que una vez que borre la linea, no me quede un "hueco" donde estaba la linea
    # Uso count=1 para que se haga una sola vez el re.sub pq hay que borrar una sola linea
    patron = r"^\s*<BanTeng:Movimiento[^>]*" + r'Importe="' + f"{monto}" + r'"[^>]*Fecha="' + f"{fecha}" + '"[^>]*/>\n'
    new_text = re.sub(patron, "", text, count=1, flags=re.MULTILINE) 

    # Acá busco la linea que tiene la cantidad de movimientos, el (\d+) es para buscar uno o más dígitos
    movimientos = re.search(r'(<BanTeng:TotalMovimientos>)(\d+)(</BanTeng:TotalMovimientos>)', new_text)
    
    # Guardo la etiqueta de <BanTeng:TotalMovimientos> en la variable etiqueta
    # Guardo la etiqueta de </BanTeng:TotalMovimientos> en la variable etiqueta_fin 
    # Esto lo hago para construir la nueva etiqueta, que lo único que le cambia es la cantidad de movimientos totales
    etiqueta = movimientos.group(1)
    cant_movimientos = movimientos.group(2)
    etiqueta_fin = movimientos.group(3)

    nueva_cant_movimientos = int(cant_movimientos) - 1

    # Guardo la linea original en la variable linea original, group(0) te da todo lo que encontró search que estaba entre parentesis en tu patrón
    linea_original = movimientos.group(0)

    # Construyo la nueva etiqueta, tenía que poner str ahí porque sino la concatenación no funcaba, porque nueva_cant_movimientos es un int
    linea_nueva = etiqueta + str(nueva_cant_movimientos) + etiqueta_fin

    # Acá uso re.sub para reemplazar la linea original por la linea nueva, y lo hago una vez sola con con count=1
    new_text = re.sub(linea_original, linea_nueva, new_text, count=1)

    return new_text

if __name__ == '__main__':
    entrada_pdf = sys.argv[1]  # archivo entrada (param)
    entrada_xml = sys.argv[2]  # archivo entrada (param)
    salida = sys.argv[3]   # archivo salida (param)    
 
    ret = programa6(entrada_pdf,entrada_xml)      # ejecutar 
    
    f = open(salida, 'w', encoding='utf-8') # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
