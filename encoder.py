from msgpack.fallback import xrange


def split(word):
    return list(word)

def rotU(char, rot):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join([abc[(abc.find(char)+rot)%26]])

def rotL(char, rot):
    abc = "abcdefghijklmnopqrstuvwxyz"
    return "".join([abc[(abc.find(char)+rot)%26]])

def hexit(char):
    return hex(ord(char)).lstrip("0x")


word = '~V01Td4Ng3R!'

chararray = split(word)
newchararray = list()
for i in reversed(xrange(chararray.__len__())):
    char=chararray[i]
    if char.islower():
        newchararray.append(hexit(rotL(char,7)))
    elif char.isupper():
        newchararray.append(hexit(rotU(char,13)))
    elif char.isdigit():
        newchararray.append(hexit(str((int(char)+7)%10)))
    else:
        newchararray.append(hexit(char))
    newchararray.append(":")

newchararray.pop(newchararray.__len__()-1)
print("".join(newchararray))


