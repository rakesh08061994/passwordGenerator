import string
import random

def passGen(level="m"):
    try:
        s1 = string.punctuation
        s2 = string.digits
        s3 = string.ascii_uppercase
        s4 = string.ascii_lowercase

        level1 = "l"
        level2 = "m"
        level3 = "h"
        level4 = "x"

        s = []

        s.extend(s1)
        s.extend(s2)
        s.extend(s3)
        s.extend(s4)
        random.shuffle(s)

        if str(level).lower() == level1:
            print("".join(s[0:9]))
        elif str(level).lower() == level2:
            print("".join(s[0:12]))
        elif str(level).lower() == level3:
            print("".join(s[0:18]))
        elif str(level).lower() == level4:
            print("".join(s[0:26]))
        else:
            print("".join(s[0:level]))

    except NameError:
        print("Input is incorrect.")


if __name__ == "__main__":
    passGen(8)
    passGen("l")
    passGen("m")
    passGen("h")
    passGen("x")
