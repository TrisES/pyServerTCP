import random
from socket import *
import threading
"""
Serveren lytter på port 12000 og venter på en forbindelse.
Når en klient forbinder, så starter den en ny tråd, som håndterer kommunikationen med klienten.
Klienten sender en besked til serveren, som så svarer alt efter hvilken metode der er angivet i beskeden.
"""

# Methods
def split_message(message):
    return message.split(";")

def handle_client(connectionSocket, addr):
    print("Connection from: " + addr[0])
    keep_communicating = True

    while keep_communicating:
        # Receive a message from the client
        sentence = connectionSocket.recv(1024).decode().strip()
        print(f"Client{addr} said: " + sentence)
        response = "Didn't understand, please send a proper message"

        # Parse the message
        method, value1, value2 = "", 0, 0
        argList = split_message(sentence)
        if (len(argList) == 3):
            value1 = int(argList[1])
            value2 = int(argList[2])
        method = argList[0]

        # Handle the message based on the method
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

        # Send the response to the client
        connectionSocket.send(response.encode())

    # Close the connection (after the loop)
    connectionSocket.close()

# "Main" (Waits for incoming connections and handles them in a new thread)
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