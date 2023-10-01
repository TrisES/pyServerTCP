import random
from socket import *
import threading

# Methods
def split_message(message):
    return message.split(";")

def handle_client(connectionSocket, addr):
    print("Connection from: " + addr[0])
    keep_communicating = True

    while keep_communicating:
        sentence = connectionSocket.recv(1024).decode().strip()
        print(f"Client{addr} said: " + sentence)
        response = "Didn't understand, please send a proper message"

        method, value1, value2 = "", 0, 0
        argList = split_message(sentence)
        if (len(argList) == 3):
            value1 = int(argList[1])
            value2 = int(argList[2])
        method = argList[0]

        match method:
            case "Random":
                if (value1 > value2):
                    response = "First value must be smaller than the second"
                else:
                    response = str(random.randint(int(value1), int(value2)))
            case "Add":
                response = str(int(value1) + int(value2))
            case "Subtract":
                if (value1 < value2):
                    response = "First value must be equal or larger than the second"
                else:
                    response = str(int(value1) - int(value2))
            case "Close":
                keep_communicating = False
                response = "closing the connection"

        connectionSocket.send(response.encode())
    connectionSocket.close() # Close the connection (after the loop)


# "Main"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(('', serverPort)) # 
serverSocket.listen(1)
print('Server is ready to listen')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handle_client, args=(connectionSocket, addr)).start()

# Noter:
# I opgaven står der: "Bemærk, i både random og subtract er rækkefølgen vigtig."
# Hvad menes der præcis med det? 
# (at ved substract, så skal tal1 være større end tal2?)
# (at ved random, så skal tal1 være mindre end tal2?)
# Eller er det bare en påmindelse om, at vi skal huske at trække tal2 fra tal1, og ikke omvendt?