#!/usr/bin/env python
"""
This is an example to show how to use SailsWebsocket library.
"""

from sails_websocket import SailsWebsocket
import time

connection_state = 0

def on_connect(ws):
    print('bitch please')
    ws.send('post', '/engine/connection/335', {"token":"token"}, {"datatopost": "data"})

def on_error(ws, error):
    print('fuuuuuuuuu')
    print(error)

def on_message(ws, message):
    global connection_state
    if (connection_state == 0) and (message == "connection_ok"):
        connection_state = 1
        print('connected')
    elif connection_state == 1:
        print(message)
    else:
        print('connection error')

if __name__ == '__main__':
    ws = SailsWebsocket('192.168.1.26:1337/socket.io')
    ws.on_connect = on_connect
    ws.on_error = on_error
    ws.on_message = on_message
    while True:
        try:
            ws.run_forever()
        except Exception as e:
            print(str(e))
        time.sleep(1)
