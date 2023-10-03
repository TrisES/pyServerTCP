# pyServerTCP
Oktober 2023, obligatorisk opgave 4+5.

## Noter
### Protokol
<img width="933" alt="image" src="https://github.com/TrisES/pyServerTCP/assets/112662675/657d0228-9570-43df-8b44-fed52a273691">

### TCP Server
Serveren lytter på port 12000 og venter på en forbindelse.
Når en klient forbinder, så starter den en ny tråd, som håndterer kommunikationen med klienten.
Klienten sender en besked til serveren, som så svarer alt efter hvilken metode der er angivet i beskeden.

### TCP Klient
Forbinder til en server på IP-adressen 127.0.0.1 på port 12000 og sender en besked til serveren.
Beskeden konstrueres ud fra brugerinput og inkluderer et metodenavn og to værdier.
Serveren svarer med en ændret besked, som klienten så udskriver til konsollen.

### JSON variant
Der er også en variant af TCP Server og Klient, som sender JSON formaterede strings i stedet for nøgne/ikke-formaterede strings.
