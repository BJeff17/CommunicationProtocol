
import socket

ADDRESSE = ("localhost",8000)


client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESSE)
print(client.recv(512).decode())


while True :

    out = client.recv(512).decode()
    print(out)
    if out=="quit":
        print("Vous vous déconnecté!")
        break
    message = input("Entrez votre message: ")
   
    client.sendall(message.encode())
    if message == "quit" :
        print("L'autre s'est déconnecté!")
        break


client.close()
