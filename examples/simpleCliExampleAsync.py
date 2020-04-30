# Blobber importieren
from blobber import blobber

# Die Funktion, welche nach erflogreicher Transaktion ausgeführt wird.
# Sie muss einen Paramenter haben, um die Payment Klasse zu erhalten.
# Mehr wird weiter unten erklärt.
def functionAfterSuccessfulTransaction(payment):
    # Es wird die Anzahl an eingezahltem Geld anzeigt
    print("Es wurde", payment.paidBalance, "von", payment.price, "eingezahlt. yay! ")

# Eine Verbindung mit Blobber wird initialisiert
# Wie erstellt man einen Blobber Dev-Token? -> https://github.com/Alone2/blobberApi#key
myConnection = blobber.Connection("DEIN BLOBBER DEV TOKEN")

# Nutzer wird gebeten einzugeben, wie viel Geld (Dogecoin) eingezahlt werden sollte.
requestPrice = int( input("Wie viele Dogecoin sollten eingezahlt werden? ") )

# Es wird eine neue Dogecoin Adresse kreiert an welche das Geld gesendet werden kann.
payment = myConnection.createPurchase(requestPrice)

# Die Adresse sowie die die Anzahl Dogecoin, welche eingezahlt werden soll, wird angezeigt
print(payment.address)
print(payment.price)

# Wir definieren, dass die Funktion functionAfterSuccessfulTransaction 
# nach erfolgreicher Einzahlung ausgeführt wird.
# (Es muss gleich viel, oder mehr, als gefordert eingezahlt werden)
payment.executeOnComplete(functionAfterSuccessfulTransaction)

# Hier kann jetzt etwas anderes im Code geschehen
# während das Programm im Hintergund wartet, bis die 
# Transaktion abgeschlossen ist und die vorher definierte 
# Funktion ausführt.
print("wait...")
