from starters.ns_console import msg_server

operations = {
    "suma":"AddServer",
    "resta":"SubServer",
    "multiplicacion":"ProductServer",
    "division":"DivServer",
    "modulo":"ModServer",
    "potencia":"PowerServer"
}

addr = None

print("Escribe ENTER para salir...")
while True:
    if not addr:
        print("¿Qué operacion desea realizar?")
        opciones = [op.capitalize() for op in list(operations.keys())]
        print( ", ".join(opciones) )
        print("Escribe la operacion: ", end="") 
        
    else:
        print("Escribe los numeros separados por comas: ")
        
    user_input = input().lower()
    
    if user_input == "exit" or user_input == "":
        if addr: addr = None
        else: break
    elif not addr:
        if user_input not in operations.keys():
            matches = [value for value in operations.keys() if user_input in value ]
            if len(matches) == 1:
                user_input = matches[0]
            else:
                print("Entrada invalida")
                continue
            
        resp = msg_server(msg=f"LOOKUP {operations[user_input]}")
        ip, port = resp.split(":")
        addr = (ip, int(port))
    else:
        resp = msg_server(msg=user_input, addr=addr)
        print(resp)