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

print("Presiona exit para salir...")
while True:
    if not addr:
        print("¿Qué operacion desea realizar?")
        opciones = operations.keys().capitalize()
        print( ", ".join(opciones) )
        print("Escribe la operacion: ", end="") 
        
    else:
        print("Escribe los numeros separados por comas: ")
        
    user_input = input().lower()
    
    if user_input == "exit" or user_input == "":
        if addr: addr = None
        else: break
    elif not addr:
        resp = msg_server(msg=f"LOOKUP {operations[user_input]}")
        ip, port = resp.split(":")
        addr = (ip, int(port))
    else:
        resp = msg_server(msg=user_input, addr=addr)
        print(resp)