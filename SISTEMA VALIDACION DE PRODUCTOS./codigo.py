print("Bienvenido a la tienda Bendicion de Dios")
print ("¿Como es tu nombre?")
miNombre = input()
print ("Es un placer tenerte por aqui "+ miNombre)
print ("En que podemos ayudarte?")

#y solicitando cuatro datos esenciales al usuario.

nombre_producto = input("Ingrese porfavor el nombre del producto que desea llevar: ")

#validacion de datos y que el programa valide sin descuento y con el descuento.
while True :
    try:
        precio_unitario = int(input("Ingrese porfavor el precio unitario: "))
        cantidad_producto = int(input("Ingrese porfavor la cantidad de producto que desea adquirir en su compra: "))
        porcentaje_descuento = int(input("Ingrese porfavor el descuento que tiene el producto(En caso de que no disponga digite 0):" ))
        costo_sin_descuento = (precio_unitario )* (cantidad_producto)
    #Valida que los datos ingresados son numeros 
        if (precio_unitario > 0 ) and (cantidad_producto > 0 ) and (porcentaje_descuento <= 100) and (porcentaje_descuento >= 1):
            costo_descuento = (costo_sin_descuento) * (porcentaje_descuento) / 100
            print ("El producto que desea llevar es",nombre_producto)
            print (f"El total con el descuento aplicado es: {costo_sin_descuento - costo_descuento:.2f}")
        else:
            costo_sin_descuento = (precio_unitario ) * (cantidad_producto)
            print ("El producto que desea llevar es",nombre_producto)
            print (f"El total de su compra es:{costo_sin_descuento:.2f}")        
        break
    except:
        print("¡Hiciste algo que no se esperaba!,(DIGITE PORFAVOR SOLO NUMEROS EN PRECIO UNITARIO Y CANTIDAD DE PRODUCTOS.)")

#Mensaje de despedida al usuario
print ("¡Gracias por su compra!")
print ("Esperamos su pronto regreso:)")
print ("¡Que tenga un excelente dia!")