import funciones as fn

pedidos = []


while True:
    print("MENU PAqExpress")
    print("1. Realizar pedido")
    print("2. Listar Pedidos")
    print("3. Imprimir Hoja de Ruta")
    print("4. Salir")
    opc_usuario = int(input("Ingrese una opción: "))
    if opc_usuario == 1:
        print()
        fn.realizar_pedido(pedidos)
    else:
        if opc_usuario == 2:
            print()
            fn.listar_pedidos(pedidos)
        else: 
            if opc_usuario == 3:
                print()
                fn.imprimir_hoja_de_ruta(pedidos)
            else:
                if opc_usuario == 4:
                    print("Saliendo de la aplicación...")
                    break

