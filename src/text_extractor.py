from sys import exit

# Convierte un documento en una lista donde cada linea es un item de esta
## path es la ruta donde tiene que buscar el archivo
def text_extractor(path):
    try:
        documento = open(path, 'r')
    except FileNotFoundError:
        exit("El documento pasado no existe")
    lineas_documento = documento.readlines()
    documento.close()

    i = 0
    for linea in lineas_documento:
        lineas_documento[i] = linea.strip('\n')
        i += 1

    assert isinstance(lineas_documento, list)

    return lineas_documento