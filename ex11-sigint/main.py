import signal
import time

is_uninterrupted = True


def stop(sig, frame):
    global is_uninterrupted
    print("SIGINT detected.")
    is_uninterrupted = False


signal.signal(signal.SIGINT, stop)


def neverendng_loop():
    while is_uninterrupted:
        time.sleep(1)


neverendng_loop()
