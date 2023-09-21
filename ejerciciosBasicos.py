# TODO: Refactorizar el código para evitar la recursividad.

def enetradaString(mensaje: str) -> input:
    return input(mensaje)
def entradaInt(mensaje: str) -> input:
    return int(input(mensaje))


def nombre() -> str: # -> str no sé si está bien puesto ya que no retorna nada.
    """ 
    Description: Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.
    
    :raises: except de prueba por si algo sale mal

    :rtype: str

    """
    try:
        nombre:str = enetradaString("Escribe aquí tu nombre: ")
        return(f"hola {nombre}" )
    except TypeError:
        raise TypeError("Algo salió mal, revisa el")

        
def importeTotalPorHoras():
    
    """ 
    Description: Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
    
    :raises: ValueError: por si no introduce un enetero.
            else por si hay algún error que no he contemplado.

    :rtype: No devuelve nada?
    """
    try:
        hora = int(input("Introduce las horas de trabajo: "))
        costePorHora = int(input("Introduce el coste por hora: "))
        print("Importe total: ",hora*costePorHora)
    except ValueError:
        print("Error 001: Por favor introduzca un número")
    elegirEjercicio()

def asignacion():

    """ 
    Description: Suponiendo que se han ejecutado las siguientes sentencias de asignación:

    Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:

    1. ancho / 2
    2. ancho // 2
    3. alto / 3
    4. 1 + 2 * 5

    :raises: todo está definido no es necesario una captura.

    :rtype:
    """

    ancho = 17
    alto = 12.0
    print(ancho/2) # La mitad de 17
    print(ancho//2) # modulo de ancho
    print(alto/3) # alto entre 3
    print(1 + 2 * 5) # primero hace la multiplicación y luego la suma
    elegirEjercicio()
 
def conversionCelsiusFahrenheit():

    """ 
    Description: Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

    :raises:

    :rtype:
    """
    try:
        celsius = int(input("Introduce una temperatura en celsuis: "))
        print((celsius * 9 / 5) + 32)
    except ValueError:
        print("Error 001: Por favor introduzca un número")
    
    finally:
        elegirEjercicio()

def ivaAplicado():

    """ 
    Description: Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.

    :raises:

    :rtype:
    """
    try:
        precio = int(input("Introduce el precio del producto: "))
        iva = int(input("introduce el tipo de iva: "))
        print(f"El producto de {precio}€ + el {iva}% es: {(precio*iva)/100 + precio}€ en total")
    except ValueError:
        print("Error 001: Por favor introduzca un número")
    finally:
        elegirEjercicio()

def desgloseProducto():

    """ 
    Description: Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

    :raises: ValueError

    :rtype: nada?
    
    """

    try:
        importeTotal = int(input("Introduzca el importe total del producto: "))
        iva = 10
        print(f"Al producto de {importeTotal}€ se ha descontando un iva del 10% (-{(importeTotal*iva)/100}€) es: {importeTotal - (importeTotal*iva)/100 }€ en total")
    except ValueError:
        print("Error 001: Por favor introduzca un número")
    finally:
        elegirEjercicio()
    
def sumaDeTresNumeros():

    """ 
    Description:  Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

    :raises: ValueError

    :rtype: nada?
    """

    try:
        primerNumero = int(input("Introduzca el primer número: "))
        segundoNumero = int(input("Introduzca el primer número: "))
        tercerNumero = int(input("Introduzca el primer número: "))
        print(f"La suma total es: {primerNumero+segundoNumero+tercerNumero}")
    except ValueError:
        print("Error 001: Por favor introduzca un número")
    finally:
        elegirEjercicio()

def sumaConDosVariables():

    """ 
    Description: Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

    :raises: ValueError

    :rtype: nada?
    """

    try:
        numeroUno = int(input("introduce el primer número: "))
        numeroUno += int(input("Introduce el segudno número: "))
        numeroDos = int(input("Introduce el tercer número: "))
        print(numeroUno+numeroDos)
    except ValueError:
        print("Error 001: Por favor introduzca un número")
    finally:
        elegirEjercicio()

def sumaSinVariables():

    """ 
    Description: ¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo.

    :raises: ValueError

    :rtype: nada?
    """

    try:
        print(int(input("introduce el primer número: ")) + int(input("Introduce el segudno número: "))+ int(input("Introduce el tercer número: ")))
    except ValueError:
        print("Error 001: Por favor introduzca un número")
    finally:
        elegirEjercicio()

def operacionAritmetica():

    """ 
    Description: Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética: 

    (3+2/2*5)^2


    :raises: no es necesario?

    :rtype: nada?
    """

    print(((3+2)/(2*5))**2)
    elegirEjercicio()

def enterosPositivos():

    """ 
    Description: Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

    suma = n(n+1)/2

    :raises:

    :rtype:
    """

    try:
        numero = int(input("Introduce un número: "))
        if numero < 0:
            raise TypeError("Error 004: El número tiene que ser positivo.")
        else:
            print(f"La suma de todos los números hasta {numero} es: {round(numero*(numero+1)/2)}")
    except (ValueError):
        print("Error 001: Por favor introduzca un número")
    except TypeError as error:
        print(error)
    finally:
        elegirEjercicio()

def indiceDeMasaCorporal():

    """ 
    Description: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

    :raises:

    :rtype:
    """

    try:
        peso = float(input("Introduce tu peso en kg: "))
        altura = float(input("Introduce tu altura en metros: "))
        imc = peso/altura
        print(f"Tu índice de masa corporal es: {round(imc, 2)}")
    # except ValueError:
    #     print("Error 001: Por favor introduzca un número")
    except ZeroDivisionError:
        print("La altura no puede ser 0.")
    finally:
        elegirEjercicio()

def division():

    """ 
    Description: Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.

    :raises:

    :rtype:
    """
    try:
        numeroUno = int(input("Introduzca el primer número: "))
        numeroDos = int(input("Introduzca el segundo número: "))

        print(f"El cociente de la división es: {numeroUno/numeroDos}, y el resto es {numeroUno%numeroDos}")
    except ValueError:
        print("Error 001: Por favor introduzca un número")
    finally:
        elegirEjercicio()

def pesoTotal():

    """ 
    Description: Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

    :raises:

    :rtype:
    """
    payaso = 112
    muñeca = 75

    try:
        numeroPayaso = int(input("Escribe el número de payasos: "))
        numeroMuñeca = int(input("Escribe el número de muñecas: "))

        print(f"El peso total del paquete es: {(numeroPayaso*payaso)+(numeroMuñeca*muñeca)}kg")
    except ValueError:
        print("Error 001: Por favor introduzca un número")
    finally:
        elegirEjercicio()

def calculoInteres():

    """ 
    Description: Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

    Calcula el interés: capital * (1 + interes)

    :raises:

    :rtype:
    """

    interes = 4
    primerAño = 1
    segundoAño = 2
    tercerAño = 3
    try:
        deposito = int(input("Ingrese la cantidad actual del depósito de ahorro: "))
        print(f"El interés total para primer año: {deposito * (primerAño+interes)}\nEl interés total para el segundo año: {deposito * (segundoAño+interes)}\nEl interés total para el tercer año: {deposito * (tercerAño+interes)}\n")
    except ValueError:
        print("Error 001: Por favor introduzca un número")
    finally:
        elegirEjercicio()




def elegirEjercicio():

    """ 
    Description: Menú para la selección de ejercicios a elección del usuario y salida del programa en caso de que el usuario así lo desee.

    :raises:

    :rtype:
    """

    try:
        print("---0: Exit---")
        print("---1: Ejercicio nombre---")
        print("---2: Ejercicio de calculo de importe total---")
        print("---3: Ejercicio de deducción de asignaciones---")
        print("---4: Ejercicio de conversión de celsius a fahrenheit---")
        print("---5: Ejercicio de aplicación de iva---")
        ejercicio = int(input("Elige un ejercicio del 1-14 \n> "))
    except ValueError:
        print("Error 001: Por favor introduzca un número")
        
    while ejercicio != 0:

        if ejercicio == 1:
            salida(nombre())
        elif ejercicio == 2:
            importeTotalPorHoras()
        elif ejercicio == 3:
            asignacion()
        elif ejercicio == 4:
            conversionCelsiusFahrenheit()
        elif ejercicio == 5:
            ivaAplicado()
        elif ejercicio == 6:
            desgloseProducto()
        elif ejercicio == 7:
            sumaDeTresNumeros()
        elif ejercicio == 8:
            sumaConDosVariables()
        elif ejercicio == 9:
            sumaSinVariables()
        elif ejercicio == 10:
            operacionAritmetica()
        elif ejercicio == 11:
            enterosPositivos()
        elif ejercicio == 12:
            indiceDeMasaCorporal()
        elif ejercicio == 13:
            division()
        elif ejercicio == 14:
            calculoInteres()

    if ejercicio < 0 or ejercicio > 14:
        print("Error 003: Introduzca un valor dentro del rango")
        elegirEjercicio()

def salida(funcion):
    print(funcion)

elegirEjercicio()