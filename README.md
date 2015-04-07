# node2mqtt

Popularność wiadomości [MQTT](http://en.wikipedia.org/wiki/MQTT) spowodowała, że powstaje wiele ciekawych projektów pozwalających na zbieranie i analizowanie danych z czujników. Ciekawym przykładem jest tu projekt [OpenHAB](http://www.openhab.org/). node2mqtt jest aplikacja przekazująca dane z czujników w postaci wiadomości MQTT do tychże programów.

## Wymagania

node2mqtt pisany był w środowisku Linuks, więc zakłada się, że działa tylko po nim. Do poprawnej pracy potrzebuje Pythona 2.x oraz kilka innych zewnętrznych aplikacji, m.in.

- python
- python-simplejson
- python-pip
- ser2net
- tornado (3.0)
- screen
- paho-mqtt

Debian wymaga jeszcze:

- python-dev
- build-essential


Przykład instalacji dla Debiana/Ubuntu:

    $ sudo apt-get install python screen git ser2net python-pip python-dev build-essential
    $ sudo pip-2.7 install simplejson tornado tornado-redis paho-mqtt


### Transmisja szeregowa (UART)

Surowe dane z czujników należy przekierować z UART do TCP. do tego celu służy aplikacja ser2net. 

Zalecane ustawienie w pliku /etc/ser2net.conf:

    2000:raw:0:/dev/ttyAMA0:9600
    
Należy pamiętać, aby ustawić ten sam port w pliku 'settings.conf' aplikacji node2mqtt ('serial','port')

## Daemon
### Konfiguracja

Pliki konfiguracyjne aplikacji znajduja sie w *static/conf*.

- settings.json - ustawienia aplikacji
- nodemap.json - mapowanie nazwy z id punktu
- control.json - konfiguracja przekaźników

### Uruchomienie

     $ cd sensmon
     $ screen -d -m python2 node2mqtt.py

### Plany

- odbiór wiadomości MQTT


# Uwaga
Aplikacja jest we wstępnym stanie rozwoju autor nie ponosi odpowiedzialności na niewłaściwe działanie programu i uszkodzenia powstałe na skutek jego działania.

## Licencja

The MIT License (MIT)

Copyright (c) 2015 Artur Wronowski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


![Valid XHTML](http://w3.org/Icons/valid-xhtml10)

