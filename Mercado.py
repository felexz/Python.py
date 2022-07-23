#3. Hacer un programa que registre el consumo realizado por los clientes de un restaurante, si el consumo de cada cliente excede 50000 se hará un descuento del 20%. Se debe mostrar el pago de cada cliente y el total de todos los pagos.


h = {" Tacos" : 27000 }
b = {" Bebida" : 12000 }
c = {" Desayuno" : 20000 }
a = {" atun" : 19000 }
v = {" Sopa" : 23000 }
m = {" Carne" : 29000 }
q = {" Pescado" : 28000 }

cesta = {}

input("  \nBienvenido al mercado virtual! \n"
"    \nA continuacion se le presentaran las opciones, presiona 'enter' para continuar!\n")

while True:
    opcion = input("\n 1) Para ver los productos y sus precios\n 2)  Para hacer una compra\n 3) Para salir\n")
    if opcion == "1":
        print("", h , "\n" , b , "\n" , c , "\n" , a , "\n" , v , "\n" , m , "\n" , q   )

    elif opcion == "3":
        print("\nSALIENDO DEL PROGRAMA...")
        break

    elif opcion == "2":
        print("iniciando compra\n")
        item = input("Introduce el articulo que quieres comprar: ")
        print("", h , "\n" , b , "\n" , c , "\n" , a , "\n" , v , "\n" , m , "\n" , q   )
        precio = float(input('Introduce el precio de ' + item + ': '))
        cesta[item] = precio
        continuar = input(" ¿Quieres añadir otro producto? (si/no)") == "si"
        if continuar == True:
            item = input("Introduce el articulo que quieres comprar: ")
            precio = float(input('Introduce el precio de ' + item + ': '))
            cesta[item] = precio
            continuar = input(" ¿Quieres añadir otro producto? (si/no)") == "si"
        if continuar == True:
            item = input("Introduce el articulo que quieres comprar: ")
        else:
            costo = 0

            print( "Lista de la compra")
            for item, precio in cesta.items():
                print(item, "\t", precio)
                costo += precio
                descuento = (30*costo) / (100)
                total_con_descuento = costo - descuento

                if costo >= 50000:
                    print("coste total:  ", total_con_descuento )

                else:
                     print("coste total:  ", costo)
