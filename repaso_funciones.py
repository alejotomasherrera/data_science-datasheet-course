def detect_type(data):
    tipo = type(data)
    return tipo

def str_manipulate(cadena):
    print("Mayuscula:", cadena.upper())
    print("Minuscula:", cadena.lower())
    print("Titulo:", cadena.title())

def funcion_count(cadena):
    count = cadena.count("a")
    print("Hay", count," 'a' en la cadena")
    replace = cadena.replace("a", "s")

def practicas_listas():
    countries = ["USA","Argentina","India","Chile","Brazil"]
    #Utilizacion de Index (Positivo y negativo)

def rebanada_silicing():
    countries = ["USA","Argentina","India","Chile","Brazil"]
    print(countries[0:2])
    # nombre_lista [start:stop]
    # Es excluyende el 2(stop excluyente)
    
    # Metodo append
    countries.append("Canada")

    # Metodo insert (posicion, elemento a insertar)
    countries.insert(0, "Alemania")
    countries = countries1 = countries2
    # Concatenacion de listas
    concatenacion_lista = countries1 + countries2

    # Eliminar elementos de una lista
    # nombre_lista.remove("elemento a eliminar")
    countries.remove("Canada")
    # nombre_lista.pop([index])
    countries.pop(0)
    # devuelve el elemento elegido por el pop: "USA"

def ordenas_listas():
    number_list = [4,2,5,6,3,7]
    number_list.sort() #Ordeno de menor a mayor
    number_list.sort(reverse=True) #Ordeno de mayor a menor

    # Acceder de forma secuencial a un index
    number = number_list[0]

    # Cambiar elemento de una lista
    number_list[0] = 1000

    # Copiar elementos de una lista
    nueva_lista = number_list.copy()

    ##Otra forma de copiar con rebanada
    nueva_lista = number_list[:]