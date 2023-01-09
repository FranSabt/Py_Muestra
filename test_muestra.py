import random
from muestra import hola, hello_world, mas_de_veinte_caracteres, suma, saludar, resta, multiplicacion, division, potencia, de_negativo_a_positivo, de_positivo_a_negativo


def test_hola(capsys):
    hola()
    stdout, stderr = capsys.readouterr()
    assert len(stdout) >= 1

def test_hello(capsys):
    hello_world()
    stdout, stderr = capsys.readouterr()
    assert stdout == "Hello World!\n"


def test_mas_de_veinte_caracteres():
    string = mas_de_veinte_caracteres()
    assert len(string) >= 20


def test_saludo():
    saludos = ["Hello", "Buenas", "Buen Día", "Aloha", "holis", "holiwiss"]
    assert saludar() in saludos


def test_suma():
    assert suma(55, 44) == 99
    a = random.randint(0,100)
    b = random.randint(0,100)
    assert suma(a, b) == a + b
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    assert suma(a, b) == a + b

def test_resta():
    assert resta(55, 44) == 11
    a = random.randint(0,100)
    b = random.randint(0,100)
    assert resta(a, b) == a - b
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    assert resta(a, b) == a - b

def test_multiplicacion():
    assert multiplicacion(7, 5) == 35 
    a = random.randint(0,100)
    b = random.randint(0,100)
    assert multiplicacion(a, b) == a * b
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    assert multiplicacion(a, b) == a * b


def test_division():
    assert division(125, 5) == 25 
    a = random.randint(0,100)
    b = random.randint(0,100)
    assert division(a, b) == a / b
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    assert division(a, b) == a / b

def test_potencia():
    assert potencia(5) == 25 
    a = random.randint(1,100)
    assert potencia(a) == a * a
    a = random.randint(1,100)
    assert potencia(a) == a * a

def test_de_negativo_a_positivo():
    assert de_negativo_a_positivo(-5) == 5 
    a = random.randint(1, 100)
    a = a * -1
    assert de_negativo_a_positivo(a) == -1 * a
    a = random.randint(1,100)
    assert de_negativo_a_positivo(a) == -1 * a

def test_de_positivo_a_negativo():
    assert de_positivo_a_negativo(5) == -5 
    a = random.randint(1, 100)
    assert de_positivo_a_negativo(a) == -1 * a
    a = random.randint(1,100)
    assert de_positivo_a_negativo(a) == -1 * a
