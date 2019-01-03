import anki_vector
from time import sleep

with anki_vector.AsyncRobot() as r:
    while(1):
        for i in [x * 0.01 for x in range(0, 100)]:
            sleep(0.05)
            r.behavior.set_eye_color(i,1)