# Imprimimos el menú en pantalla
#contorlador que desde la consola ejecuta el registro e ingreso con credenciales, faltaria la implementacion en conjunto con
#el framework
print("""
    1) Registro con credenciales       3) Pedir viaje
    2) Ingreso a cuenta        4) Mas...
    """)

seleccion=input("-Ingresa el numero a elegir :")
correo=input("Ingresar correo")
usuario=input("Ingresar usuario")
contraseña=input("Ingresar contraseña")

if seleccion=="1":
    print("Correo: ",correo)
    print("contraseña:",contraseña)
elif seleccion=="2":
    print("Ingresa a tu cuenta:")
    print("Usuario:",usuario)
    print("contraseña:",contraseña)
elif seleccion=="3":
    print("Viajes cercanos a ti: Hay 1 conductor con espacio disponible cerca de ti")
elif seleccion=="4":
    print("otra opción")
else:
    print("Opción no válida")