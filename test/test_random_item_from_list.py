from src.random_item_from_list import random_item_from_list
import pytest

@pytest.mark.random_item_from_list
def test_funciona():
    lista = ["a","b","c","d","e","f","g","h","i","j"]
    assert random_item_from_list(lista) in lista

@pytest.mark.random_item_from_list
def test_lista_vacia():
    assert random_item_from_list([]) == ''