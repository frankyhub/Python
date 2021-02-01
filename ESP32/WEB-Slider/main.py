"""
Board: ESP32 R32
Funktion: main.py WEB-Server schaltete die interne LED (alternativ ein Relais) 
USB: CH340
https://github.com/frankyhub/Arduino-Beispiele_I/tree/master/CH341SER%20Serieller%20Treiber%20NANO
Flash: esp32-idf3-20210125-unstable-v1.13-283-g203e1d2a6.bin
https://micropython.org/download/esp32/
khf 30.01.2021

"""

def web_page():
  if relay.value() == 1:
    relay_state = ''
  else:
    relay_state = 'checked'
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>
  body{font-family:Arial; text-align: center; margin: 0px auto; padding-top:30px;}
  
  .switch{position:relative;display:inline-block;width:120px;height:68px}
  .switch input{display:none} 

  .slider{position:absolute;top:0;left:0;right:0;bottom:0;background-color:#2196f3;border-radius:34px}
  .slider:before{position:absolute;content:"";height:52px;width:52px;left:60px;bottom:8px;background-color:#fff;-webkit-transition:.4s;transition:.4s;border-radius:68px}
  
  input:checked+.slider{background-color:#ccc}
  input:checked+.slider:before{-webkit-transform:translateX(-52px);-ms-transform:translateX(-60px);transform:translateX(-52px)}
  </style>
  
  <script>function toggleCheckbox(element) { var xhr = new XMLHttpRequest(); if(element.checked){ xhr.open("GET", "/?relay=on", true); }
  else { xhr.open("GET", "/?relay=off", true); } xhr.send(); }</script></head><body>
  <h1>Hauptschalter</h1>
  <label class="switch"><input type="checkbox" onchange="toggleCheckbox(this)" %s><span class="slider">
  </span></label>

  </body></html>""" % (relay_state)
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  try:
    if gc.mem_free() < 102000:
      gc.collect()
    conn, addr = s.accept()
    conn.settimeout(3.0)
    print('Verbindung %s' % str(addr))
    request = conn.recv(1024)
    conn.settimeout(None)
    request = str(request)
    print('Inhalt = %s' % request)
    relay_on = request.find('/?relay=on')
    relay_off = request.find('/?relay=off')
    if relay_on == 6:
      print('Licht AUS')
      relay.value(0)
    if relay_off == 6:
      print('Licht EIN')
      relay.value(1)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
  except OSError as e:
    conn.close()
    print('Verbindung geschlossen')
