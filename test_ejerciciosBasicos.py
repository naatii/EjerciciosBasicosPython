import pytest
from ejerciciosBasicos import *

def test_nombre():
    assert nombre("natlia") == "hola natlia"
    # assert nombre(" ") == "hola  "
    # assert nombre(True) == "hola True"
def test_importeTotalPorHoras():
    assert importeTotalPorHoras(12, 12) == ("Importe total: ", 144)
def test_asignacion():
    assert (f"{17/2}\n{17//2}\n{12.0/3}\n{1 + 2 * 5}")
def test_desgloseProducto():
    iva: int = 10
    assert desgloseProducto(122) == (f"Al producto de {122}€ se ha descontando un iva del 10% (-{(122*iva)/100}€) es: {122 - (122*iva)/100 }€ en total")