# recurso para las letras -> https://fsymbols.com/generators/carty/

# Entrada
def enetradaString(mensaje: str) -> str:

    """ 
    Description: Función para la entrada de datos del programa siempre que sea un string o una cadena

    :type mensaje:str:
    :param mensaje:str:

    :raises:

    :rtype:
    """

    return input(mensaje)
def entradaInt(mensaje: str) -> int:

    """ 
    Description: Función para la entrada de datos del programa siempre que sea un entero o int

    :type mensaje:str:
    :param mensaje:str:

    :raises:

    :rtype:
    """

    return int(input(mensaje))
def entradaFloat(mensaje: str) -> float:

    """ 
    Description: Función para la entrada de datos del programa siempre que sea un float o decimal

    :type mensaje:str:
    :param mensaje:str:

    :raises:

    :rtype:
    """

    return float(input(mensaje))

# Lógica
def nombre() -> str:
    """ 
    Description: Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.
    
    :raises: except de prueba por si algo sale mal

    :rtype: str

    """
    try:
        nombre = enetradaString("Escribe aquí tu nombre: ")
        if nombre != " " and nombre != True:
            return(f"hola {nombre}")
    except TypeError:
        raise TypeError("Algo salió mal, revisa el código")
           
def importeTotalPorHoras() -> str:
    
    """ 
    Description: Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
    
    :raises: ValueError: por si no introduce un enetero.
            else por si hay algún error que no he contemplado.

    :rtype: No devuelve nada?
    """
    try:
        hora: int = entradaInt("Introduce las horas de trabajo: ")
        costePorHora: int =  entradaInt("Introduce el coste por hora: ")
        return("Importe total: ",hora*costePorHora)
    except ValueError:
        print("Error 001: Por favor introduzca un número")

def asignacion() -> str:

    """ 
    Description: Suponiendo que se han ejecutado las siguientes sentencias de asignación:

    Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:

    1. ancho / 2  La mitad de 17
    2. ancho // 2 modulo de ancho
    3. alto / 3 alto entre 3
    4. 1 + 2 * 5 primero hace la multiplicación y luego la suma

    :raises: todo está definido no es necesario una captura.

    :rtype:
    """

    ancho: int = 17
    alto: float = 12.0
    return(f"{ancho/2}\n{ancho//2}\n{alto/3}\n{1 + 2 * 5}") 
 
def conversionCelsiusFahrenheit() -> str:

    """ 
    Description: Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

    :raises:

    :rtype:
    """
    try:
        celsius: int = entradaInt("Introduce una temperatura en celsuis: ")
        return(f"La temperatura es de: {(celsius * 9 / 5) + 32}")
    except ValueError:
        raise ValueError("Error 001: Por favor introduzca un número")

def ivaAplicado() -> str:

    """ 
    Description: Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.

    :raises:

    :rtype:
    """
    try:
        precio: int = entradaInt("Introduce el precio del producto: ")
        iva: int = entradaInt("introduce el tipo de iva: ")
        return(f"El producto de {precio}€ + el {iva}% es: {(precio*iva)/100 + precio}€ en total")
    except ValueError:
        raise ValueError("Error 001: Por favor introduzca un número")
    
def desgloseProducto() -> str:

    """ 
    Description: Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

    :raises: ValueError

    :rtype: nada?
    
    """

    iva: int = 10
    try:
        importeTotal: int = entradaInt("Introduzca el importe total del producto: ")
        return(f"Al producto de {importeTotal}€ se ha descontando un iva del 10% (-{(importeTotal*iva)/100}€) es: {importeTotal - (importeTotal*iva)/100 }€ en total")
    except ValueError:
        raise ValueError("Error 001: Por favor introduzca un número") 
    
def sumaDeTresNumeros() -> str:

    """ 
    Description:  Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

    :raises: ValueError

    :rtype: nada?
    """

    try:
        primerNumero: int = entradaInt("Introduzca el primer número: ")
        segundoNumero: int = entradaInt("Introduzca el primer número: ")
        tercerNumero: int =  entradaInt("Introduzca el primer número: ")
        
        return(f"La suma total es: {primerNumero+segundoNumero+tercerNumero}")
    except ValueError:
        raise ValueError("Error 001: Por favor introduzca un número")
    
def sumaConDosVariables() -> int:

    """ 
    Description: Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

    :raises: ValueError

    :rtype: nada?
    """

    try:
        numeroUno : int = entradaInt("introduce el primer número: " + entradaInt("Introduce el segudno número: "))
        numeroDos: int =  entradaInt("Introduce el tercer número: ")
        return(numeroUno+numeroDos)
    except ValueError:
        return ValueError("Error 001: Por favor introduzca un número")
    
def sumaSinVariables():

    """ 
    Description: ¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo.

    :raises: ValueError

    :rtype: nada?
    """

    try:
        return(entradaInt("introduce el primer número: ")) + entradaInt("Introduce el segudno número: ")+ entradaInt("Introduce el tercer número: ")
    except ValueError:
        raise ValueError("Error 001: Por favor introduzca un número")
    
def operacionAritmetica() -> float:

    """ 
    Description: Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética: 

    (3+2/2*5)^2


    :raises: no es necesario?

    :rtype: nada?
    """

    return(((3+2)/(2*5))**2)

def enterosPositivos() -> int:

    """ 
    Description: Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

    suma = n(n+1)/2

    :raises:

    :rtype:
    """

    try:
        numero: int = entradaInt("Introduce un número: ")
        if numero < 0:
            raise TypeError("Error 004: El número tiene que ser positivo.")
        else:
            return(f"La suma de todos los números hasta {numero} es: {round(numero*(numero+1)/2)}")
    except ValueError:
        raise ValueError("Error 001: Por favor introduzca un número")
    except TypeError as error:
        raise(error)

def indiceDeMasaCorporal() -> float:

    """ 
    Description: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

    :raises:

    :rtype:
    """

    try:
        peso : float = entradaFloat("Introduce tu peso en kg: ")
        altura: float = entradaFloat("Introduce tu altura en metros: ")
        imc: float = peso/altura
        return(f"Tu índice de masa corporal es: {round(imc, 2)}")
    # except ValueError:
    #     print("Error 001: Por favor introduzca un número")
    except ZeroDivisionError:
        raise ZeroDivisionError("La altura no puede ser 0.")
    
def division() -> str:

    """ 
    Description: Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.

    :raises:

    :rtype:
    """
    try:
        numeroUno = entradaInt("Introduzca el primer número: ")
        numeroDos = entradaInt("Introduzca el segundo número: ")

        return(f"El cociente de la división es: {numeroUno/numeroDos}, y el resto es {numeroUno%numeroDos}")
    except ValueError:
        raise ValueError("Error 001: Por favor introduzca un número")
    
def pesoTotal() -> str:

    """ 
    Description: Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

    :raises:

    :rtype:
    """
    payaso: int = 112
    muñeca: int = 75

    try:
        numeroPayaso = entradaInt("Escribe el número de payasos: ")
        numeroMuñeca = entradaInt("Escribe el número de muñecas: ")

        return(f"El peso total del paquete es: {(numeroPayaso*payaso)+(numeroMuñeca*muñeca)}kg")
    except ValueError:
        raise ValueError("Error 001: Por favor introduzca un número")
    
def calculoInteres() -> str:

    """ 
    Description: Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

    Calcula el interés: capital * (1 + interes)

    :raises:

    :rtype:
    """

    interes: int = 4
    primerAño: int = 1
    segundoAño: int = 2
    tercerAño: int = 3
    try:
        deposito = entradaInt("Ingrese la cantidad actual del depósito de ahorro: ")
        return(f"El interés total para primer año: {deposito * (primerAño+interes)}\nEl interés total para el segundo año: {deposito * (segundoAño+interes)}\nEl interés total para el tercer año: {deposito * (tercerAño+interes)}\n")
    except ValueError:
        raise ValueError("Error 001: Por favor introduzca un número")
    
def panadería():
    
        """
        Description: Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.

        :raises:
    
        :rtype:
        """

def elegirEjercicio():
    """ 
    Description: Menú para la selección de ejercicios a elección del usuario y salida del programa en caso de que el usuario así lo desee.

    :raises:

    :rtype:
    """

    textoMenu = """ 
    ~ 𝟘: 𝔼𝕩𝕚𝕥                                                        
    ~ 𝟙: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕟𝕠𝕞𝕓𝕣𝕖                                           
    ~ 𝟚: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕔𝕒𝕝𝕔𝕦𝕝𝕠 𝕕𝕖 𝕚𝕞𝕡𝕠𝕣𝕥𝕖 𝕥𝕠𝕥𝕒𝕝                
    ~ 𝟛: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕕𝕖𝕕𝕦𝕔𝕔𝕚𝕠́𝕟 𝕕𝕖 𝕒𝕤𝕚𝕘𝕟𝕒𝕔𝕚𝕠𝕟𝕖𝕤            
    ~ 𝟜: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕔𝕠𝕟𝕧𝕖𝕣𝕤𝕚𝕠́𝕟 𝕕𝕖 𝕔𝕖𝕝𝕤𝕚𝕦𝕤 𝕒 𝕗𝕒𝕙𝕣𝕖𝕟𝕙𝕖𝕚𝕥 
    ~ 𝟝: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕒𝕡𝕝𝕚𝕔𝕒𝕔𝕚𝕠́𝕟 𝕕𝕖 𝕚𝕧𝕒                    
    ~ 𝟞: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕕𝕖𝕤𝕘𝕝𝕠𝕤𝕖 𝕕𝕖 𝕡𝕣𝕠𝕕𝕦𝕔𝕥𝕠
    ~ 𝟟: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕤𝕦𝕞𝕒𝕣 𝟛 𝕟𝕦́𝕞𝕖𝕣𝕠𝕤 𝕔𝕠𝕟 𝟛 𝕧𝕒𝕣𝕚𝕒𝕓𝕝𝕖𝕤
    ~ 𝟠: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕤𝕦𝕞𝕒𝕣 𝟛 𝕟𝕦́𝕞𝕖𝕣𝕠𝕤 𝕔𝕠𝕟 𝟚 𝕧𝕒𝕣𝕚𝕒𝕓𝕝𝕖𝕤
    ~ 𝟡: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕤𝕦𝕞𝕒𝕣 𝟛 𝕟𝕦́𝕞𝕖𝕣𝕠𝕤 𝕔𝕠𝕟 𝕤𝕚𝕟 𝕧𝕒𝕣𝕚𝕒𝕓𝕝𝕖𝕤
    ~ 𝟙𝟘: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕠𝕡𝕖𝕣𝕒𝕔𝕚𝕠́𝕟 𝕒𝕣𝕚𝕥𝕞𝕖́𝕥𝕚𝕔𝕒
    ~ 𝟙𝟙: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕤𝕦𝕞𝕒𝕣 𝕕𝕖 𝕝𝕠𝕤 𝕟𝕦́𝕞𝕖𝕣𝕠𝕤 𝕙𝕒𝕤𝕥𝕒 𝕟
    ~ 𝟙𝟚: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕔𝕒𝕝𝕔𝕦𝕝𝕠 𝕕𝕖 𝕀𝕄ℂ
    ~ 𝟙𝟛: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕕𝕚𝕧𝕚𝕤𝕚𝕠́𝕟
    ~ 𝟙𝟜: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕡𝕖𝕤𝕠 𝕥𝕠𝕥𝕒𝕝 𝕕𝕖𝕝 𝕡𝕒𝕢𝕦𝕖𝕥𝕖
    ~ 𝟙𝟝: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕔𝕒𝕝𝕔𝕦𝕝𝕠 𝕕𝕖 𝕚𝕟𝕥𝕖𝕣𝕖𝕤𝕖𝕤
    ~ 𝟙𝟞: 𝔼𝕛𝕖𝕣𝕔𝕚𝕔𝕚𝕠 𝕕𝕖 𝕝𝕒 𝕡𝕒𝕟𝕒𝕕𝕖𝕣𝕚́𝕒
    """
    
    
    print(textoMenu)
    functions = [exit, nombre, importeTotalPorHoras, asignacion, conversionCelsiusFahrenheit, ivaAplicado, desgloseProducto, sumaDeTresNumeros, sumaConDosVariables, sumaSinVariables, operacionAritmetica, enterosPositivos, indiceDeMasaCorporal, division, pesoTotal, calculoInteres]

    try:
        menu_items = dict(enumerate(functions, start=0))
        ejercicio = int(input("Elige un ejercicio del 1-16 \n> "))
        selected_value = menu_items[ejercicio]
        salida(selected_value())
    except ValueError:
        raise ValueError("Error 003: Introduzca un valor dentro del rango" if ejercicio < 0 or ejercicio > 16 else elegirEjercicio())
    except UnboundLocalError:
        raise UnboundLocalError("Error 001: Por favor introduzca un número")
    
# Salida
def salida(funcion):
    print(funcion)
    elegirEjercicio()


if __name__ == "__main__":
    elegirEjercicio()