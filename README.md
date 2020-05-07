# blobberApi


## Inhaltsverzeichnis
1. [Was ist blobberApi?](#exp)
1. [Warum funktioniert blobberApi nicht?](#why)
1. [Installation](#installation)
1. [Erste Schritte](#steps)
1. [Blobber Dev-Token](#key)
1. [Wie Dogecoin mit Blobber?](#dog)
1. [Warnung wärend Verwenden von blobbApi](#war)
1. [BlobberServerError](#bse)
1. [Ist Blobber sicher?](#security)

## Was ist blobberApi / Blobber? <a name="exp"></a>
Wichtig: Blobber und blobberApi ist nur für Testzwecke und das Kennenlernen von Kryptowährungen geeignet.

Mit blobberApi und Blobber ist es möglich, ganz einfach ein Dogecoin Zahlungssystem mit Python zu erstellen.

## Warum funktioniert blobberApi nicht? <a name="why"></a>
Ich habe das Modul noch nie getestet.

## Installieren <a name="installation"></a>
Clone dieses git repo und installiere das Modul mit pip:
```pip install .``` oder ```python -m pip install .```

Wichtig: Es wird Python 3 nicht 2 verwendet!

## Erste Schritte <a name="steps"></a> 

Beispiele zur Verwendung der Library sind im 'examples' Ordner zu finden.

1. Command-Line Beispiel, welches im Vordergrund auf eine Zahlung wartet -> [link](https://github.com/Alone2/blobberApi/blob/master/examples/simpleCliExample.py)
1. Command-line Beispiel, welches im Hintergrund auf eine Zahlung wartet -> [link](https://github.com/Alone2/blobberApi/blob/master/examples/simpleCliExampleAsync.py )

## Erstellung eines Blobber Dev-Token <a name="key"></a>
1. Gehe auf [blobber.ch](https://blobber.ch), logge dich ein, oder registriere dich.
1. Wenn angemeldet, klicke oben bei 'Upload', 'Send' und 'Other' auf 'Other'. 
1. Unten auf diesem Tab ist der Dev-Token notiert.

## Wie sende ich Geld an eine Dogecoin Adresse mit Blobber? <a name="dog"></a>
Es ist möglich eine normale Dogecoin Wallet zu verwenden. Man sendet die Dogecoin einfach an die gegebene Adresse.

Die Alternative ist, Dogecoin auf [Blobber](blobber.ch) hochzuladen und so Transaktionen durchzuführen. 
Das hat den Vorteil, dass keine Gebühr für die Transaktion bezahlt werden muss, falls der Empfänger Blobber verwendet.


## Warnungen werden angezeigt, wenn ich die blobberApi brauche. Was bedeutet das? <a name="war"></a>
Es kann sein, dass Warnungen wie "InsecureRequestWarning" wärend dem Benutzen von bloberApi angezeigt werden. 
Das ist normal, zeigt aber jedoch auf, dass die Sicherheitsstandarts von Blobber nicht unbedingt den besten entsprechen.

### Bedeutet das, dass Blobber unsicher ist?
Ja. Siehe [hier](#security)

## Bei mir erscheint der BlobberServerError, was heisst das?  <a name="bse"></a>
Entweder wurde der Blobber Dev Token nicht richtig eingegeben (siehe [hier](#key)), oder es ga einen Fehler auf dem Blobber Server.

## Ist Blobber sicher? <a name="security"></a>
[Nein](https://blobber.ch#news-BenutzenSieBlobberundDogecoinalsZahlungsmittelaufIhrerWebseite)

## Warum ist Blobber zum Teil auf Deutsch und zum Teil auf Englisch? 
Because I'm too lazy to implement a solution to handle multiple languages.
