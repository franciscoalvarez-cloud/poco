#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video],
productos={"8475HD":["HP",15.6,"8GB","DD","1T","Intel Core i5","Nvidia GTX1050"],
           "2175HD":["lenovo",14,"4GB","SSD","512GB","Intel Core i5","Nvidia GTX1050"],
           "JjfFHD":["Asus",14,"16GB","SSD","256GB","Intel Core i7","Nvidia RTX2080Ti"],
           "fgdxFHD":["HP",15.6,"8GB","DD","1T","Intel Core i3","integrada"],
           "GF75HD":["Asus",15.6,"8GB","DD","1T","Intel Core i7","Nvidia GTX1050"],
           "123FHD":["lenovo",14,"6GB","DD","1T","AMD Ryzen 5","integrada"],
           "342FHD":["lenovo",15.6,"8GB","DD","1T","AMD Ryzen 7","Nvidia GTX1050"],
           "UWU131HD":["Dell",15.6,"8GB","DD","1T","AMD Ryzen 3","Nvidia GTX1050"],
           }
#stock = {modelo: [precio, stock], ...]
stock={"8475HD":["HP",450850,6],"2175HD":["lenovo",958990,35],"JjfFHD":["Asus",764320,15],"fgdxFHD":["HP",550900,10],
       "GF75HD":["Asus",325000,2],"123FHD":["lenovo",250900,40],"342FHD":["lenovo",880990,25],"UWU131HD":["Dell",399870,5],
       }

opc=0


def búsqueda_precio(p_min, p_max):
    dicionario_filtrado={}
    for clave in stock:
        if stock[clave][1]>=p_min and stock[clave][1]<=p_max:
            dicionario_filtrado[clave]=stock[clave]
        return dicionario_filtrado


def filtar_por_precio():
    while True:
        try:
            p_min=int(input("ingrese el precio minimo del noteboot: "))
            p_max=int(input("ingrese el precio maximo del noteboot: "))
            if p_min<=10000 and p_max>=12000000:
                print("ingrese un precio dentro del rango")
                continue
            dicionario_filtrado=búsqueda_precio(p_min,p_max)
            print(f"hay {len(dicionario_filtrado)} noteboot en el rango de precio de {p_min,p_max}")
            for stock in dicionario_filtrado.values():
                print(f"Marca:{stock[0]},Moledo:{len(stock)}")
            break
        except ValueError:
            print("solo se pueden ingresar numeros enteros")








while True:
    print("*"*10,"MENU PRINCIPAL","*"*10)
    print("1)_STOCK por marca")
    print("2)_Busqueda por precio")
    print("3)_Actualizar precio")
    print("4)_salir")
    
    opc=int(input("Elija una opcion (1-4): "))

    match opc:
        case 1:
            filtar_por_precio()