from src.text_extractor import text_extractor
from src.random_item_from_list import random_item_from_list
from src.print_on_console import print_on_console

# Muestra en pantalla una linea al azar del documento pasado
## path es una variable que guarda la ruta del documento que vamos a utilizar
def random_line_from_text(path):

    lineas_documento = text_extractor(path)

    linea_documento  = random_item_from_list(lineas_documento)
    
    print_on_console(linea_documento)

path  = './data/archivo.txt'

random_line_from_text(path)