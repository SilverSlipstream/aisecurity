import aisecurity.utils.socket_ as socket_
import websocket

from aisecurity.utils.events import in_dev

@in_dev("real_time_recognize_socket is in production")
def real_time_recognize_socket(socket_url):
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(socket_url,
                              on_message = lambda ws,msg: socket_.on_message(ws, msg),
                              on_error = socket_.on_error,
                              on_close = socket_.on_close,
                              on_open = lambda ws: socket_.on_open(ws, use_picam=True))
    print("here")
    ws.run_forever()

real_time_recognize_socket("ws://172.31.217.136:8000/v1/guard/live")