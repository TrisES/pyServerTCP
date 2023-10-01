from socket import *

"""
Forbinder til en server på IP-adressen 127.0.0.1 på port 12000 og sender en besked til serveren.
Beskeden konstrueres ud fra brugerinput og inkluderer et metodenavn og to værdier.
Serveren svarer med en ændret besked, som klienten så udskriver til konsollen.
Til sidst sender klienten en 'Close' besked til serveren og lukker forbindelsen.
"""

serverName = "127.0.0.1" #IPadressen
serverPort = 12000 #Port som serveren lytter på
clientSocket = socket(AF_INET, SOCK_STREAM) #definerer socket objekt. Her ipv4 og TCP
clientSocket.connect((serverName, serverPort)) #sender en forbindelses besked afsted til Ipadresse og den valgte port.

# Spørger brugeren om input, og send det til serveren. "Metode;Tal1;Tal2"
method = input('Input method: ')
value1 = input('Input value1: ')
value2 = input('Input value2: ')
sentence = method + ";" + value1 + ";" + value2
clientSocket.send(sentence.encode()) #gør besked til bytes og send det.
modifiedSentence = clientSocket.recv(1024) #Modtager max 1024 bytes fra serveren.
print('From server: ', modifiedSentence.decode())

# Vent på bruger trykker noget, før den sender Close besked til serveren.
input("Press Enter to continue...")

clientSocket.send('Close'.encode()) # Close besked til serveren, inden den lukker forbindelsen.
clientSocket.close() # lukker forbindelsen