import autopy
import time

while True:
    autopy.mouse.toggle(True)
    time.sleep(0.01)
    autopy.mouse.toggle(False)
