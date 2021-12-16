import random

# Selecciona al azar un item de la lista pasada
## lista_lineas es un lista de las lineas del doc. pasado en la funcion anterior
## la cual puede tener cualquier tipo de variable, no discriminamos👍
def random_item_from_list(lineas_documento):
    
    assert isinstance(lineas_documento, list)

    if lineas_documento == []: return ''

    linea_documento = random.choice(lineas_documento)

    assert isinstance(linea_documento, str)

    return linea_documento