strinput = input("Enter your message:")
binmsg = list(map(bin,bytearray(strinput, 'utf8')))
print(binmsg)
for i, chars in enumerate(binmsg):
    chars = list(chars)
    chars.pop(1)
    binmsgary = "".join(chars)
    binmsg[i] = binmsgary
print(binmsg)
msgdata = "".join(binmsg)
print(msgdata)