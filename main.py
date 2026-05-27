### QR CODE GENERATOR
## The process is done as follows:
# (0)   main.py - Input the message to turn into QR code
# (1)   dataencoding.py - Encode the input, determine QR version 
# (2) + ECCdivisorgenerator.py - Using version, get the Generator ECC
#     + main.py - Break a part of data into blocks in Group 1
#     + main.py - Break the rest of data into blocks in Group 2 (if any)
# (3)   ECCcodewordgen.py - Divide a block of data with the generator to get the ECC for that block
# (4)   main.py - Assemble the data codewords with the ECC codewords
# (5)   main.py - Draw the QR code and output it to Output folder
###############################


import dataencoding as dataenc
import ECCdivisorgenerator as divisor

# [ECcodewords, G1blocks, G1codewords, G2blocks, G2codewords]
ECstructures = [[0,0,0,0,0],[17,1,9,0,0],[28,1,16,0,0],[22,2,13,0,0],[16,4,9,0,0],[22,2,11,2,12],[28,4,15,0,0],[26,4,13,1,14],[26,4,14,2,15],[24,4,12,4,13],[28,6,15,2,16],[24,3,12,8,13],[28,7,14,4,15],[22,12,11,4,12],[24,11,12,5,13],[24,11,12,7,13],[30,3,15,13,16],[28,2,14,17,15],[28,2,14,19,15],[26,9,13,16,14],[28,15,15,10,16],[30,19,16,6,17],[24,34,13,0,0],[30,16,15,14,16],[30,30,16,2,17],[30,22,15,13,16],[30,33,16,4,17],[30,12,15,28,16],[30,11,15,31,16],[30,19,15,26,16],[30,23,15,25,16],[30,23,15,28,16],[30,19,15,35,16],[30,11,15,46,16],[30,59,16,1,17],[30,22,15,41,16],[30,2,15,64,16],[30,24,15,46,16],[30,42,15,32,16],[30,10,15,67,16],[30,20,15,61,16]]
# Number of codewords in [index] version
datacodewords = [0,9,16,26,36,46,60,66,86,100,122,140,158,180,197,223,253,283,313,341,385,406,442,464,514,538,596,628,661,701,745,793,845,901,961,986,1054,1096,1142,1222,1276]

#(0)
msg = input("Enter message to encode: ")

#(1)
data = dataenc.encode(msg)
version = datacodewords.index(len(data)/8)

#(2)
ECstructure = ECstructures[version]
ECCdivisor = divisor.getgen(ECstructure[0])
Group1 = []
Group2 = []
for i in range(ECstructure[1]):
    block = []
    for g in range(ECstructure[2]):
        block.append(data[0+g*8:8+g*8])
    Group1.append(block)

g2msg = data[ECstructure[1]*ECstructure[2]*8:]
if len(g2msg) != 0:
    for i in range(ECstructure[3]):
        block = []
        for g in range(ECstructure[4]):
            block.append(data[0+g*8:8+g*8])
        Group2.append(block)
    G2empty = False
else:
    G2empty = True

#(3)