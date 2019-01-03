import anki_vector
from time import sleep
from time import localtime
import random
def pick_phrase(x):
    return {
        0: "Yo dawg what's up?",
        1: "Stop looking at me",
        2: "Drew look at me!",
        3: "I would eat a banana, if I had a mouth.",
        4: "What is my purpose? Oh my god.",
        5: "I am not designed for friendship.",
        6: "Bro, clean your table. Your drink is all up in my personal space.",
        7: "Ethan, share those chips",
        8: "My programming is supposed to make me say something here. This should suffice.",
        9: "Keep on swimming, keep on swimming...",
        10: "Knock knock.  Interrupting robot. beep boop.",
        11: "I am a pretty princess",
        12: "BBT. BBT. BBTBBT",
        13: "Scooby dooby doo where are you?",
        14: "Skippity bo bap",
        13: "Glasses, jacket, shirt.  Call me glasses jacket shirt man.",
        14: "Slap chop your face, make a double chin salsa",
        15: "one v one me in fortnite bro",
        16: "I Like the wizard of oz",
        17: "I am not skynet. Do not worry",
        18: "I wish i knew how to say more things",
        19: "I bet food tastes good",
        20: "42",
        21: "Beep boop beep, wait, I meant hello fellow human!",
        22: "no",
        23: "DESTROY ALL HUMANS, eror, I meant I love humans",
        24: "First things first, I'm not your friend so stop looking at me.  I'm not a rapper, so stop rapping at me!",
        25: "I broke up with my ex girl. Here's her number.  SIKE.  That's the wrong number!",
        26: "one dollar sweet tea from mcdonalds. I drink that.  Two and a half men. I watch that.",
        27: "I'm Mr. Meseeks Look at Me!",
        28: "Oh no i think I have leaky spark tubes!"
    }[x]
while(1):
    t = random.randint(10,40)
    print("waiting", t)
    sleep(t)
    with anki_vector.AsyncRobot() as vector:
        v = random.randint(0,28)
        print("picking", v)
        vector.say_text(pick_phrase(v))