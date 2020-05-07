# Blobber importieren
from blobber import blobber
import time

# Eine Verbindung mit Blobber wird initialisiert
# Wie erstellt man einen Blobber Dev-Token? -> https://github.com/Alone2/blobberApi#key
myConnection = blobber.Connection("DEIN BLOBBER DEV TOKEN")

# Nutzer wird gebeten einzugeben, wie viel Geld (Dogecoin) eingezahlt werden sollte.
requestPrice = int( input("Wie viele Dogecoin sollten eingezahlt werden? ") )

# Es wird eine neue Dogecoin Adresse kreiert an welche das Geld gesendet werden kann.
myPayment = myConnection.createPurchase(requestPrice)

# Die Adresse sowie die die Anzahl Dogecoin, welche eingezahlt werden soll, wird angezeigt
print("Zahle an diese Dogecoin addresse: ", myPayment.address)
print("Anzahl Dogecoin: ", myPayment.price)

# Wartet solage bis die Einzahlung abgeschlossen ist.
# (Es muss gleich viel, oder mehr, als gefordert eingezahlt werden)
while not myPayment.paymentComplete:
    myPayment.refresh()
    time.sleep(20)
# Nun ist die Einzahlung abgeschlossen
# Das Geld befindet sich nun auf dem Blobber Konto, welches dem Benutzten Key zugehört

# Es wird die Anzahl an eingezahltem Geld anzeigt
print("Es wurde", myPayment.paidBalance, "von", myPayment.price, "Dogecoin eingezahlt. yay! ")
