# Character capacities & codeword number lookup table - ECC H LEVEL
cap = [0,7,14,24,34,44,58,64,84,98,119,137,155,177,194,220,250,280,310,338,382,403,439,461,511,535,593,625,658,698,742,790,842,898,958,983,1051,1093,1139,1219,1273]
datacodewords = [0,9,16,26,36,46,60,66,86,100,122,140,158,180,197,223,253,283,313,341,385,406,442,464,514,538,596,628,661,701,745,793,845,901,961,986,1054,1096,1142,1222,1276]
## MODE: BYTE (1)
mode = "0100"

strinput = input("Enter your message: ")
length = len(strinput)
if length == 0:
    print("Error: message empty")
    exit()
elif length > 1273:
    print("Error: Character limit of 1273 exceeded")
    exit()

# Find suitable type
type = 0
while length > cap[type]:
    type += 1

## CHARACTER LENGTH NOTATION (2)
# remove "b" from the bin value
lenotation = list(bin(length))
lenotation = lenotation[2:]
lenotation = "".join(lenotation)
# find required length
if type < 10:
    notlen = 8
else:
    notlen = 16
# pad to length
lenotation = "0" * (notlen - len(lenotation)) + lenotation

## Convert msg to bin (3)
binmsg = list(map(bin,bytearray(strinput, 'utf8')))
for i, chars in enumerate(binmsg):
    chars = list(chars)
    chars = chars[2:]
    binmsgary = "".join(chars)
    if len(binmsgary) % 8 != 0:
        binmsgary = "0" * (8 - len(binmsgary)) + binmsgary
    binmsg[i] = binmsgary
msgdata = "".join(binmsg)

## Merge the data (1)(2)(3)
data = mode + lenotation + msgdata

## Add terminator (4)
if (datacodewords[type] * 8) - len(data) > 4:
    data += "0000"
    finished = False
else:
    data += "0" * ((datacodewords[type] * 8) - len(data))
    finished = True # data is filled and needs no further modification

## Padding in case data is NOT finished
if not finished:
    # add 0s to make length a multi of 8
    if (len(data) % 8) != 0:
        data += "0" * (8 - len(data))
    # add pad bytes
    ipad = 1
    while (len(data) != (datacodewords[type]) * 8):
        if ipad % 2 == 1:
            data += "11101100"
        else:
            data += "00010001"
        ipad += 1

## Final data
print("type:",type)
print("mode:",mode)
print("length notation:",lenotation)
print("message bits:",msgdata)
print("pads:", ipad)
print("final data:", data)