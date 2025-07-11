productos =  {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}


stock = {'8475HD': [387990,10], '2175HD': [327990,4],
'JjfFHD': [424990,1],'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0] }

def stock_marca(marca):
    total = 0
    for modelo, datos in productos.items():
        if datos [0].lower() == marca.lower() and modelo in stock:
            total = total+ stock[modelo][1]
    print(f'El stock es: {total}')


def busqueda_precio(precio_min, precio_max):
    disponibles=[]
    for modelo,datos in stock.items():
        precio,cantidad=datos
        if precio_min<=precio<=precio_max and cantidad>0:
            marca=productos[modelo][0]
            disponibles.append(f'{marca} -- {modelo}')
    if disponibles:
        print('los computadores disponibles son: ',sorted(disponibles))
    else:
        print('no hay computadores disponibles')

def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0]=nuevo_precio
        return True
    else:
        return False

while True:
    print("****Menú Principal****")
    print("1. Stock marca.")
    print("2. Busqueda por precio.")
    print("3. Actualizar precio.")
    print("Salir.")
    
    opcion = int(input("Ingrese una opción del menu: "))
    
    if opcion == 1:
            marca = input("ingrese marca a consultar: ").lower().strip()
            stock_marca(marca)
        
    elif opcion == 2:
        while True:
            try:
                precio_min = int(input("Ingrese el rango de precio minimo a buscar: "))
            except:
                print('Debe ingresar numeros enteros')
            try:
                precio_max = int(input("Ingrese el rango de precio minimo a buscar: "))
            except:
                print('Debe ingresar numeros enteros')
                
            busqueda_precio(precio_min, precio_max)
            break
        
    elif opcion ==3:
        while True:
            modelo =input('Ingrese el modelo a actualizar: ')
            try:
                nuevo_precio=int(input('ingrese el nuevo precio'))
                if actualizar_precio(modelo,nuevo_precio):
                    print('Precio actualizado')
                else:
                    print('El modelo no existe')
            except:
                print('debe ingresar un valor numerico para el precio')
            continuar=input('desea actualizar el precio de otro producto (si/no)?').lower()
            if continuar!='si':
                break
            
    elif opcion == 4:
            print("Programa finalizado...")
            break
            
    else:
        print("Debe seleccionar una opción válida!!! (1-4)")
        
        
        
        
        
        
    
        


        
        
    
    

    
    
    

