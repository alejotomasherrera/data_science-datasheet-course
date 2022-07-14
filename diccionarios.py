def diccionarios():
    mi_diccionario = {"key1":"value1","key2":"value2"}
    my_data = {"nombre":"Alejo","edad":26}
    print(my_data["nombre"])

    # Metodo keys para diccionarios
    ## diccionario.keys -> dict_keys(["key1", "key2"])
    print(my_data.keys())
    
    # Metodo values para diccionarios
    ## diccionario.values -> dict_values(["value1","value2"])
    print(my_data.values())

    # Agregar/actualziar elementos
    my_data["estatura"] = 1.7
    print(my_data)

    # Agregar con metodo update
    my_data.update({"estatura":1.8,"lenguajes":["Ingles", "Español","Portuges"]})
    print(my_data)

    # Copiar un diccionario (Es independiente al diccionario original)
    diccionario_copia = my_data.copy()

    # Eliminar elementos de un diccionario con pop
    my_data.pop("estatura")
    print(my_data)

    # Eliminar elementos con out
    del my_data["lenguajes"]
    print(my_data)

    # Vaciar un diccionario con clear
    my_data.clear()
    print(my_data)
diccionarios()