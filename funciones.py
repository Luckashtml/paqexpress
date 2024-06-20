PEDIDO = ['pequeño','mediano','grande']
SECTOR = ['centro','norte','sur']

def realizar_pedido(pedidos):
    nombre = input("Ingrese su nombre y apellido: ")
    direccion = input("Ingrese su dirección: ")
    sector = input("Ingrese el sector de su comuna (Norte / Centro / Sur ): ").lower()
    while sector not in SECTOR:
        print ("Comuna no identificada, ingrese nuevamente")
        sector = input("Ingrese el sector de su comuna (Norte / Centro / Sur ): ").lower()
    detalle_pedido = input("Ingrese el detalle del pedido (pequeño / mediano / grande): ").lower()
    while detalle_pedido not in PEDIDO:
        print("Pedido no identificado. Intente nuevamente")
        detalle_pedido = input("Ingrese el detalle del pedido (pequeño / mediano / grande): ").lower()
    
    pedidos.append({
        "Nombre": nombre,
        "Direccion": direccion,
        "Sector": sector,
        "DetallePedido": detalle_pedido
    })
    print ("Pedido realizado con éxito")



def listar_pedidos(pedidos):
    for pedido in pedidos:
        print (pedidos)

def imprimir_hoja_de_ruta(pedidos):
    sector_pedido = input("Ingrese el sector de la comuna a imprimir (Norte / Centro / Sur ): ").lower()
    if sector_pedido in SECTOR:
        pedido_imprimir = []
        for pedido in pedidos:
            if pedido['Sector'] == sector_pedido:
                pedido_imprimir.append(pedido)
                nombre_archivo = f"pedido_sector_{sector_pedido}.txt"
    else:
        print ("Sector no encontrado")
        return
    
    with open(nombre_archivo,'w') as archivo:
            for pedido in pedidos:
                archivo.write(f"Nombre: {pedido['Nombre']}\n")
                archivo.write(f"Direccion: {pedido['Direccion']}\n")
                archivo.write(f"Sector: {pedido['Sector']}\n")
                archivo.write(f"Detalle Pedido: {pedido['DetallePedido']}\n")

    
                
    
            
        
                    

                       

        

        


