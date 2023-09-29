# TODO: Constantes en mayúsuclas

# Constantes

ERROR001:str = "Error 001: Por favor introduzca un número"
ERROR002:str = "Error 002: Introduzca un valor dentro del rango"
ERROR003:str = "Error 003: El número tiene que ser positivo."
ERROR004:str = "Error 004: Es imposible dividir entre 0"
ERRORDESCONOCIDO:str = "Error desconocido: algo salió mal"

# Entrada   
def entradaString(mensaje: str) -> str:
    """Lee la entrada de datos de tipo String
    ---

    ---
    Args:
        mensaje (str): El mensaje que recibe el usuario para los diferentes ejercicios

    Returns:
        str: De devuelve el valor para la entrada de datos String
    """

    return input(mensaje)
def entradaInt(mensaje: str) -> int:
    """Lee la entrada de datos de tipo entero
    ---

    ---
    Args:
        mensaje (str): El mensaje que recibe el usuario para los diferentes ejercicios

    Returns:
        int: De devuelve el valor para la entrada de datos de tipo int
    """

    return int(input(mensaje))
def entradaFloat(mensaje: str) -> float:
    """Lee la entrada de datos de tipo entero
    ---

    Args:
        mensaje (str): El mensaje que recibe el usuario para los diferentes ejercicios

    Returns:
        float: De devuelve el valor para la entrada de datos de tipo float
    """


    return float(input(mensaje))

# Lógica
def nombre() -> str:
    """Description: Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.
    ---

    ---
    Raises:
        TypeError: Realmente no sé si sería correcto el uso del TypeError aquí.

    Returns:
        str: Retorno de la frase esperada según las especificaciones del ejercicio.
    """        

    try:
        nombre:str = entradaString("Escribe aquí tu nombre: ")
        if nombre != " " and nombre != True:
            return(f"hola {nombre}")
    except TypeError:
        raise TypeError(ERRORDESCONOCIDO)
           
def importeTotalPorHoras() -> str:
    """Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
    ---

    Raises:
        ValueError: por si no introduce un enetero.

    Returns:
        str: Retorno del importe total del servicio.
    """    
    
    try:
        hora: int = entradaInt("Introduce las horas de trabajo: ")
        costePorHora: int =  entradaInt("Introduce el coste por hora: ")
        return("Importe total: ",hora*costePorHora)
    except ValueError:
        raise ValueError(ERROR001)

def asignacion() -> str:
    """Suponiendo que se han ejecutado las siguientes sentencias de asignación:

    Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:

    1. ancho / 2  La mitad de 17
    2. ancho // 2 modulo de ancho
    3. alto / 3 alto entre 3
    4. 1 + 2 * 5 primero hace la multiplicación y luego la suma
    ---

    Returns:
        str: diferentes operaciones con el ancho y el alto para intentar adivinar que devuelve antes de verlo.
    """    
    

    ancho: int = 17
    alto: float = 12.0
    return(f"{ancho/2}\n{ancho//2}\n{alto/3}\n{1 + 2 * 5}") 
 
def conversionCelsiusFahrenheit() -> str:
    """Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
    ---

    ---
    Raises:
        ValueError: Control para la entrada de datos de tipo int.

    Returns:
        str: Temperatura en Fahrenheit.
    """    

    try:
        celsius: int = entradaInt("Introduce una temperatura en celsuis: ")
        return(f"La temperatura es de: {(celsius * 9 / 5) + 32}")
    except ValueError:
        raise ValueError(ERROR001)

def ivaAplicado() -> str:
    """Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
    ---

    ---
    Raises:
        ValueError: Control para la entrada de datos de tipo int.

    Returns:
        str: Precio con iva aplicado según el usuario.
    """    

    try:
        precio: int = entradaInt("Introduce el precio del producto: ")
        iva: int = entradaInt("introduce el tipo de iva: ")
        return(f"El producto de {precio}€ + el {iva}% es: {(precio*iva)/100 + precio}€ en total")
    except ValueError:
        raise ValueError(ERROR001)
    
def desgloseProducto() -> str:
    """Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

    Raises:
        ValueError: Captura de error para la entrada de datos de tipo int

    Returns:
        str: Desglose del producto con iva mostrando el iva y el precio sin éste.
    """

    iva: int = 10
    try:
        importeTotal: int = entradaInt("Introduzca el importe total del producto: ")
        return(f"Al producto de {importeTotal}€ se ha descontando un iva del 10% (-{(importeTotal*iva)/100}€) es: {importeTotal - (importeTotal*iva)/100 }€ en total")
    except ValueError:
        raise ValueError(ERROR001) 
    
def sumaDeTresNumeros() -> str:
    """Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

    Raises:
        ValueError: Captura de errores de entrada de datos de tipo int.

    Returns:
        str: Las suma de 3 números introducidos por el usuario.
    """    
    

    try:
        primerNumero: int = entradaInt("Introduzca el primer número: ")
        segundoNumero: int = entradaInt("Introduzca el primer número: ")
        tercerNumero: int =  entradaInt("Introduzca el primer número: ")
        
        return(f"La suma total es: {primerNumero+segundoNumero+tercerNumero}")
    except ValueError:
        raise ValueError(ERROR001)
    
def sumaConDosVariables() -> int:
    """Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

    Raises:
        ValueError: Captura de error para la entrada de datos de tipo int.

    Returns:
        int: La suma de 3 números con solo 2 variables.
    """

    try:
        numeroUno : int = entradaInt("introduce el primer número: " + entradaInt("Introduce el segudno número: "))
        numeroDos: int =  entradaInt("Introduce el tercer número: ")
        return(numeroUno+numeroDos)
    except ValueError:
        raise ValueError(ERROR001)
    
def sumaSinVariables() -> str:
    """¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo

    Raises:
        ValueError: Captura de errores para la entrada de datos de tipo int.

    Returns:
        str: La suma de 3 números sin utilizar variables.
    """

    try:
        return(entradaInt("introduce el primer número: ")) + entradaInt("Introduce el segudno número: ")+ entradaInt("Introduce el tercer número: ")
    except ValueError:
        raise ValueError(ERROR001)
    
def operacionAritmetica() -> float:
    """Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética: 

    (3+2/2*5)^2

    Returns:
        float: Resultado de realizar la ecuación mencionada en la descripción.
    """    

    return(((3+2)/(2*5))**2)

def enterosPositivos() -> int:
    """Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

    suma = n(n+1)/2

    Raises:
        TypeError: Error de creación propia ya que el número según las especificaciones del ejercicio no podía ser negativo.
        ValueError: Captura de error para la entrada de datos de tipo int.

    Returns:
        int: Sumatorio de todos los números hasta el número introducido por el usuario.
    """
    try:
        numero: int = entradaInt("Introduce un número: ")
        if numero < 0:
            raise TypeError(ERROR003)
        else:
            return(f"La suma de todos los números hasta {numero} es: {round(numero*(numero+1)/2)}")
    except ValueError:
        raise ValueError(ERROR001)
    except TypeError as error:
        raise(error)

def indiceDeMasaCorporal() -> float:
    """Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

    Raises:
        ZeroDivisionError: Captura de error por si el usuario introduce un cero en el dividendo.

    Returns:
        float: Retorno del IMC.
    """    
    try:
        peso : float = entradaFloat("Introduce tu peso en kg: ")
        altura: float = entradaFloat("Introduce tu altura en metros: ")
        imc: float = peso/altura
        return(f"Tu índice de masa corporal es: {round(imc, 2)}")
    # except ValueError:
    #     print(ERROR001)
    except ZeroDivisionError:
        raise ZeroDivisionError(ERROR004)
    
def division() -> str:
    """Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.

    Raises:
        ValueError: Captura de error para la entrada de datos de tipo int.
        ZeroDivisionError: Captura de error por si el usuario introduce un 0 en el dividendo.

    Returns:
        str: Devuelve el cociente y el resto de la división.
    """    
    try:
        numeroUno = entradaInt("Introduzca el primer número: ")
        numeroDos = entradaInt("Introduzca el segundo número: ")

        return(f"El cociente de la división es: {numeroUno/numeroDos}, y el resto es {numeroUno%numeroDos}")
    except ValueError:
        raise ValueError(ERROR001)
    except ZeroDivisionError:
        raise ZeroDivisionError(ERROR004)
    
def pesoTotal() -> str:
    """Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

    Raises:
        ValueError: Captura de error para la entrada de datos del tipo int.

    Returns:
        str: El peso total del paquete que será enviado.
    """    
    
    payaso: int = 112
    muñeca: int = 75

    try:
        numeroPayaso = entradaInt("Escribe el número de payasos: ")
        numeroMuñeca = entradaInt("Escribe el número de muñecas: ")

        return(f"El peso total del paquete es: {(numeroPayaso*payaso)+(numeroMuñeca*muñeca)}kg")
    except ValueError:
        raise ValueError(ERROR001)
    
def calculoInteres() -> str:
    """Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

    Calcula el interés: capital * (1 + interes)

    Raises:
        ValueError: Captura de error para la entrada de datos del tipo int.

    Returns:
        str: Interés del depósito introducido por el usuario tras 1 año, 2 y 3 años respectivamente
    """    
    

    interes: int = 4
    primerAño: int = 1
    segundoAño: int = 2
    tercerAño: int = 3
    try:
        deposito = entradaInt("Ingrese la cantidad actual del depósito de ahorro: ")
        return(f"El interés total para primer año: {deposito * (primerAño+interes)}\nEl interés total para el segundo año: {deposito * (segundoAño+interes)}\nEl interés total para el tercer año: {deposito * (tercerAño+interes)}\n")
    except ValueError:
        raise ValueError(ERROR001)
    
def panaderia() -> str:
    """Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.

    Raises:
        ValueError: Captura de error para la entrada de datos de tipo int.

    Returns:
        str: El precio total de las barras de pan que no son del día con el descuento aplicado.
    """
    
    panNormal = 3.49
    descuento = 60
    
    try:
        barras = entradaInt("Introduce la cantidad de pan que quieres comprar: ")
    
        return (f"La barra de pan normal sale a {panNormal}€, con el descuento del {descuento}% sale a {barras*descuento/100}€")
    except ValueError:
        raise ValueError(ERROR001)

def spamNombre() -> str:
    """Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

    Raises:
        TypeError: Captura de algún error, por si acaso ( no sé si está bien )

    Returns:
        str: El nombre repetido n veces.
    """    
    
    try:

        nombre = entradaString("Escribe tu nombre: ")
        spam = entradaInt("Introduce el número de veces que quieres que se repita: ")

        return (nombre + "\n")*spam
    except TypeError:
        raise TypeError(ERRORDESCONOCIDO)

def nombreCompleto() -> str:
    """Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

    Raises:
        ValueError: En caso de que algo falle pues lanzar un error

    Returns:
        str: Retorno del nombre completo en minúsculas, mayúsculas y con la primera letra en mayúsculas.
    """

    try:
        nombreCompleto: str = entradaString("Introduzca su nombre completo: ")
        nombreCompletoEnMinusculas = nombreCompleto.lower()
        nombreCompletoEnMayusculas = nombreCompleto.upper() 
        nombreCompletoEnCapitalice = nombreCompleto.title()
        return (f"El nombre en minusculas: {nombreCompletoEnMinusculas}\nNombre completo en mayúsculas: {nombreCompletoEnMayusculas}\nNombre completo con la primera en mayúsculas: {nombreCompletoEnCapitalice}")
    except ValueError: 
        raise ValueError(ERRORDESCONOCIDO)

def letrasNombre() -> str:
    try:
        pass
    except ValueError:
        raise ValueError(ERRORDESCONOCIDO)

def elegirEjercicio():
    """Menú para la selección de ejercicios a elección del usuario y salida del programa en caso de que el usuario así lo desee.

    Raises:
        ValueError: Captura de error para la entrada de datos de tipo int
        UnboundLocalError: Esto es porque el menú cuando introduces un número que no está contemplado saca este error.
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
    functions = [exit, nombre, importeTotalPorHoras, asignacion, conversionCelsiusFahrenheit, ivaAplicado, desgloseProducto, sumaDeTresNumeros, sumaConDosVariables, sumaSinVariables, operacionAritmetica, enterosPositivos, indiceDeMasaCorporal, division, pesoTotal, calculoInteres, panaderia, spamNombre, nombreCompleto, letrasNombre]

    try:
        menu_items = dict(enumerate(functions, start=0))
        ejercicio = int(input(f"Elige un ejercicio del 1-{len(functions)-1} \n> "))
        selected_value = menu_items[ejercicio]
        salida(selected_value())
    except ValueError:
        raise ValueError(ERROR002 if ejercicio < 0 or ejercicio > len(functions) else elegirEjercicio())
    except UnboundLocalError:
        raise UnboundLocalError(ERROR001)
    
# Salida
def salida(funcion):
    """Salida de datos del programa, con una llamada recurrente a elegirEjercicio() para que el programa continue.

    Args:
        funcion (funion): Recibe una función como parametro para imprimirla por consola.
    """    

    print(funcion)
    elegirEjercicio()

if __name__ == "__main__":
    elegirEjercicio()