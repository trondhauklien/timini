# Bilde-script for timini.no
Er det flere enn meg som synes det er kjipt å laste opp ett og ett bildet til galleriene på timini.no?   
Frykt ikke, jeg kommer med det glade budskap.  

Dette simple Python-skriptet gjør opplastingen til en lek.  
Jeg har testet det på både Windows og macOS, skal fungere greit.
Kan kjøres i terminal/cmd ved å skrive

~~~
python imagebot.py
~~~

Forutsetter at du har Python installert på datamaskinen din.  
En annen mulighet er å åpne det i f.eks. VS Code og kjøre det i terminalen der.  

Skriptet bruker Python-biblioteket requests, som kanskje må installeres hvis det ikke er gjort fra før:  

~~~
python -m pip install requests
~~~

Når du kjører skriptet vil du bli bedt om å lime inn url-en til opplastningssiden til galleriet ditt,   
f.eks. [https://www.timini.no/gallery/upload/130341](https://www.timini.no/gallery/upload/130341)

Deretter kan du dra en mappe inn i terminalvinduet ditt. Skriptet vil forsøke å laste opp alle filene i mappen.

Skriptet vil liste opp alle filene og du blir bedt om å bekrefte at du vil fortsette.

Skriv inn brukernavn og passord. (Passordet blir ikke vist, men skrives likevel inn.)

Bildene lastes opp.
