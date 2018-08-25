#!/usr/bin/env python
import qrcode
from tempfile import NamedTemporaryFile
import tkinter as tk
import http.server as server
import random
from threading import Thread
import sys
import os
import urllib.parse
import socket

ip = socket.gethostbyname(socket.gethostname())

if len(sys.argv < 2):
    print(f'Usage:\n $ {argv[0]} /path/to/game.cia')
    exit(1)

# If no external IP was detected there is no point to continue
if not len(ip) or ip.split('.')[0] == '127':
    print('Failed to detect external ip address. Sorry for that.')
    exit(1)

# Moving to cia's location
cia = sys.argv[1]
cia_name = cia.split(os.sep)[-1]
cia_path = cia.replace(cia_name,'')
os.chdir(cia_path)

# Binding to random port to allow multiple copies running
# there is slim chance to fail here, but i'll leave it as it is
# for simplicity's sake
port = random.randint(20000, 40000)
url = f'http://{ip}:{port}/{urllib.parse.quote(cia_name)}'


# Starting server on first detected external IP
# too bad for you if first detected ip is vpn or similar
handler = server.SimpleHTTPRequestHandler
s = server.HTTPServer(('',port), handler)
thread = Thread(target=s.serve_forever)
thread.start()

# Creating QR Code image and saving it in temp file
img = qrcode.make(url)
tmp = NamedTemporaryFile()
img.save(tmp)

# Creating window to show qr code
root = tk.Tk()
canvas = tk.Canvas(root, width=img.height, height=img.height)
canvas.pack()
img = tk.PhotoImage(file=tmp.name)
canvas.create_image(0, 0, image=img)
tk.mainloop()

# Shutting down server after image was closed
# It will serve all existing connections though,
# so it is save to close window before download is finished
s.shutdown()