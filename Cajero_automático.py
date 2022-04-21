clave_del_usuario = "1313"
monto_total = 10000

while True:
    usuario = input("Ingrese su clave: ")
    if usuario == clave_del_usuario:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta. Inténtelo de nuevo.")
        continue

while True:
    print("")
    print("Menú")
    print("Puede elegir entre las siguientes acciones:")
    print("")
    print("1.Retirar")
    print("2.Ver saldo")
    print("3.Salir")
    
    accion = input("¿Qué acción desea realizar? (1-3): ")

    if accion == "1":
        
        cantidades_retiros = ["", 20, 50, 100, 150, 500]

        while True:

            print("Seleccione el monto que desea retirar:")
            print("1.S/20")
            print("2.S/50")
            print("3.S/100")
            print("4.S/150")
            print("5.S/500")
            print("6.Ingresar otro monto")

            try:
                monto_seleccionado = int(input("Ingrese su elección (1-6): "))

            except ValueError:
                print("El valor ingresado no es un número, intentelo de nuevo.")
                continue

            if monto_seleccionado > 0 and monto_seleccionado < 6:
                monto_retiro = cantidades_retiros[monto_seleccionado]

            elif monto_seleccionado == 6:
                try:
                    monto_retiro = int(input("Indique el monto exacto que desea retirar: "))
                
                except ValueError:
                    print("El valor ingresado no es un número, por favor ingrese una cantidad valida.")

                if monto_retiro <= 0:
                    print("El monto a retirar no puede igual o menor que 0")
                    continue

            else:
                print("El número ingresado no esta dentro del rango de opciones")
                continue 

            if monto_retiro > monto_total:
                print("Operación rechazada. No puede retirar una cantidad mayor a su monto actual")
                continue
            
            monto_total = monto_total - monto_retiro

            while True:
                visualizar_monto = input("¿Desearía visualizar su monto restante? 1.Sí  2.No: ")
                if visualizar_monto == "1":
                    print("Su monto restante es S/{}".format(monto_total))
                    break
                elif visualizar_monto == "2":
                    break
                else:
                    print("El valor ingresado no esta dentro del rango de opciones")
                    continue
            
            break
                
    elif accion == "2":
        print("Su monto actual es S/{}".format(monto_total))
        continue

    elif accion == "3":
        print("Gracias por escoger nuestro servicio. ¡Hasta pronto!")
        break

    else:
        print("El valor ingresado no esta dentro del rango de opciones")
        continue
    






            



