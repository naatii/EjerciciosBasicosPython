from ejerciciosBasicos import *

def test_nombre(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "natalia") # Simula la entrada de datos por consola
    assert nombre() == "hola natalia"
    # assert nombre(" ") == "hola  "
    # assert nombre(True) == "hola True"
def test_importeTotalPorHoras(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda hora: "12")
    monkeypatch.setattr('builtins.input', lambda costePorHora: "12")
    assert importeTotalPorHoras() == ("Importe total: ", 144)
def test_asignacion():
    assert (f"{17/2}\n{17//2}\n{12.0/3}\n{1 + 2 * 5}")
def test_conversionCelsiusFahrenheit(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda celsius: "12")
    assert conversionCelsiusFahrenheit() == "La temperatura es de: 53.6"
def test_ivaAplicado(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda precio: '12')
    monkeypatch.setattr('builtins.input', lambda iva: '12')
    assert ivaAplicado() == "El producto de 12€ + el 12% es: 13.44€ en total"
def test_desgloseProducto(monkeypatch):
    iva: int = 10
    monkeypatch.setattr('builtins.input', lambda importeTotal: "122")
    
    assert desgloseProducto() == (f"Al producto de {122}€ se ha descontando un iva del 10% (-{(122*iva)/100}€) es: {122 - (122*iva)/100 }€ en total")
def test_sumaDeTresNumeros(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda primerNumero: '12')
    monkeypatch.setattr('builtins.input', lambda segundoNumero: '12')
    monkeypatch.setattr('builtins.input', lambda tercerNumero: '12')
    assert sumaDeTresNumeros() == ("La suma total es: 36")
def test_sumaConDosVariables(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda primerNumero: '12')
    monkeypatch.setattr('builtins.input', lambda _: '12')
    monkeypatch.setattr('builtins.input', lambda tercerNumero: '12')
    assert sumaDeTresNumeros() == ("La suma total es: 36")
def test_sumaSinVariables(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '12')
    monkeypatch.setattr('builtins.input', lambda _: '12')
    monkeypatch.setattr('builtins.input', lambda _: '12')
    assert sumaDeTresNumeros() == ("La suma total es: 36")
    
    assert indiceDeMasaCorporal() == "Tu índice de masa corporal es: 1.0"
def test_operacionAritmetica():
    assert operacionAritmetica() == 0.25
def test_enterosPositivos(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda numero: "12")
    assert enterosPositivos() == "La suma de todos los números hasta 12 es: 78"
def test_imc(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda peso: '12')
    monkeypatch.setattr('builtins.input', lambda altura: "12")
def test_division(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda numerouno: "12")
    monkeypatch.setattr('builtins.input', lambda numeroDos: "12")
    assert division() == "El cociente de la división es: 1.0, y el resto es 0"
def test_pesoTotal(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda numerouno: "12")
    monkeypatch.setattr('builtins.input', lambda numeroDos: "12")
    assert pesoTotal() == "El peso total del paquete es: 2244kg"
def test_calculoInteres(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda numerouno: "12")
    assert calculoInteres() == ("El interés total para primer año: 60\nEl interés total para el segundo año: 72\nEl interés total para el tercer año: 84\n")
def test_panaderia(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda barras: '12')
    assert panaderia() == (f"La barra de pan normal sale a 3.49€, con el descuento del 60% sale a 7.2€")
# def test_spamNombre(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda nombre: 'Natalia')
#     monkeypatch.setattr('builtins.input', lambda spam: '5')
#     assert spamNombre() == ("Natalia\nNatalia\nNatalia\nNatalia\nNatalia")

















