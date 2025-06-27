comprador={"Marcos.A":["M","Tmnt32"],
           "Juan.S":["M","Wysr54"]}
opcion="0"

def comfirmarcodigo(codigo):
    contador_mayusculas=0
    contador_numeros=0
    
    for letra in str(codigo):
        if letra.isupper():
            contador_mayusculas+=1
        if letra.isnumeric():
            contador_numeros+=1
    if contador_mayusculas<1:
        print("el codigo debe tener minimo 1 mayuscula ")
        return False
    elif contador_numeros<2:
        print("el codigo debe tener minimo 2 numeros")
        return False
    elif len(codigo)<6:
        print("el codigo debe tener minimo 6 caracteres")
        return False
    else:
        return True
    
def solicitarcodigo():
    while True:    
        codigo=input("ingrese el codigo del boleto: ")
        if comfirmarcodigo(codigo)==True:
            print("codigo registrado")
            break
        else:
            print("codigo invalido intente denuevo")
    return codigo

def tipodeentrada():
    while True:
        entrada=input("ingrese tipo de entrada (G/V): ")
        if entrada!="G" or entrada!="V":
            print("entrada invadila intente denuevo")
            return False
        else:
            elecion=entrada
            print("ENTRADA REGISTRADA")
            elecion
            return True

def ingresarcompra():
        nombre=input("ingrese el nombre del comprador: ")
        codigo=solicitarcodigo()
        entrada=tipodeentrada()
        
        boleta=[nombre,entrada,codigo]
        return boleta
    
def buscarcompardor(nombre):
    compradorencontrado=None
    for boleta in comprador:
        if boleta["nombre"]==nombre:
            compradorencontrado==boleta
            break
    return compradorencontrado

def guardarboleta(nombre,entrada,codigo):
    if buscarcompardor(nombre)==None:
        nuevaboleta={"nombre":nombre["entrada":entrada,"codigo":codigo]}
        comprador.append(nuevaboleta)
    else:
        print("este comprador ya existe")

def mostrarcomprador(nombre):
    mostrarcomprador=buscarcompardor(nombre)
    if mostrarcomprador!=None:
        print("-"*60)
        print(f"tipo de entrada: {mostrarcomprador["entrada"]}\tcodigo: {mostrarcomprador["codigo"]}")
        print("-"*60)
    else:
        print("este comprador no existe")


def eliminarcompra(nombre):
    mostrarcomprador=buscarcompardor(nombre)
    if mostrarcomprador!=None:
        indicecomprador=comprador.index(mostrarcomprador)
        del comprador[indicecomprador]
        print("¡COMPRA CANCELADA¡")
    else:
        print("No se pudo cancelar la compra")


while opcion!="4":
    print("-"*25,"menu del concierto el Conejo Simpático","-"*25)
    print("1)_comprar entrada")
    print("2)_Consultar comprador")
    print("3)_Cancelar compra")
    print("4)_salir")
    try:    
        opcion=input("ingrese la opcion que desea (1-4): ")
    except ValueError:
        print("NO SE PUEDEN INGRESAR LETRAS")

    match opcion:
        case "1":
            mostrarcomprador=ingresarcompra()
            if mostrarcomprador!=None:
                guardarboleta(nombre)
        case "2":
            nombre=buscarcompardor
            if nombre!=None:
                mostrarcomprador()
        case "3":
            nombreboleta=input("ingrese el nombre de la persona:")
            eliminarcompra(nombreboleta)
        case "4":
            print("terminar progama")
    