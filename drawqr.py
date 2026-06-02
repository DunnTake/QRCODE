import tkinter as tk
import os

def output(version,data,name):
    ### PREPARING PROPERTIES
    # Version properties 
    properties = [0, 0, [(6, 18), 11], [(6, 22), 11], [(6, 26), 11], [(6, 30), 11], [(6, 34), 11], [(6, 22, 38), 11], [(6, 24, 42), 11], [(6, 26, 46), 11], [(6, 28, 50), 11], [(6, 30, 54), 11], [(6, 32, 58), 11], [(6, 34, 62), 11], [(6, 26, 46, 66), 11], [(6, 26, 48, 70), 11], [(6, 26, 50, 74), 11], [(6, 30, 54, 78), 11], [(6, 30, 56, 82), 11], [(6, 30, 58, 86), 11], [(6, 34, 62, 90), 11], [(6, 28, 50, 72, 94), 5], [(6, 26, 50, 74, 98), 5], [(6, 30, 54, 78, 102), 5], [(6, 28, 54, 80, 106), 5], [(6, 32, 58, 84, 110), 5], [(6, 30, 58, 86, 114), 5], [(6, 34, 62, 90, 118), 5], [(6, 26, 50, 74, 98, 122), 5], [(6, 30, 54, 78, 102, 126), 5], [(6, 26, 52, 78, 104, 130), 5], [(6, 30, 56, 82, 108, 134), 5], [(6, 34, 60, 86, 112, 138), 5], [(6, 30, 58, 86, 114, 142), 5], [(6, 34, 62, 90, 118, 146), 5], [(6, 30, 54, 78, 102, 126, 150), 5], [(6, 24, 50, 76, 102, 128, 154), 5], [(6, 28, 54, 80, 106, 132, 158), 5], [(6, 32, 58, 84, 110, 136, 162), 5], [(6, 26, 54, 82, 110, 138, 166), 5], [(6, 30, 58, 86, 114, 142, 170), 5]]
    codesize = 17 + 4 * version
    fullsize = codesize + 8
    if version == 1:
        pixelsize = 11
    else:
        pixelsize = properties[version][1]
    canvasscale = pixelsize * fullsize
    align = []
    separators = []

    # Version 1 does not have alignment patterns
    if version > 1:
        nums = properties[version][0]
        seps = [(nums[0],nums[0]),(nums[-1],nums[0]),(nums[0],nums[-1])]
        for i in range(len(nums)):
            for g in range(len(nums)):
                # Exclusively avoids the separators
                cords = (nums[i],nums[g])
                if cords not in seps:
                    align.append(((nums[i]+7)*pixelsize - 1,(nums[g]+7)*pixelsize - 1))

    # Separators, coords as bottom right dot (white dot)
    separators.append((12 * pixelsize - 1,12 * pixelsize - 1))
    separators.append((canvasscale - 3 * pixelsize - 1,12 * pixelsize - 1))
    separators.append((12 * pixelsize - 1,canvasscale - 3 * pixelsize - 1))

    ### PREPARING CANVAS
    ## -- Initialize canvas
    root = tk.Tk()
    canvas = tk.Canvas(root, width=canvasscale, height=canvasscale, bg="white")
    canvas.pack()

    img = tk.PhotoImage(width=canvasscale, height=canvasscale)
    canvas.create_image(canvasscale // 2, canvasscale  // 2, image=img)
    img.put("white", to=(0,0,canvasscale-1,canvasscale-1))
    root.update()
    ## -- Drawing function

    def draw(type, start): # "dot"/"align"/"separator" as type, (x,y) as starting point
        # takes starting point as bottom right pixel
        if type == "dot":
            end = (start[0]-pixelsize + 1,start[1]-pixelsize + 1)
            img.put("black", to=(end[0],end[1],start[0]+1,start[1]+1))
        elif type == "align":
            #black 5x5
            end = (start[0]-5*pixelsize + 1,start[1]-5*pixelsize + 1)
            img.put("black", to=(end[0],end[1],start[0]+1,start[1]+1))
            #white 3x3
            end = (start[0]-4*pixelsize + 1,start[1]-4*pixelsize + 1)
            img.put("white", to=(end[0],end[1],start[0]-pixelsize+1,start[1]-pixelsize+1))
            #black center
            draw("dot",(start[0]-2*pixelsize,start[1]-2*pixelsize))
        
        elif type == "separator":
            #white 9x9 (ignore)
            #black 7x7
            end = (start[0]-8*pixelsize + 1,start[1]-8*pixelsize + 1)
            img.put("black", to=(end[0],end[1],start[0]-pixelsize+1,start[1]-pixelsize+1))
            #white 5x5
            end = (start[0]-7*pixelsize + 1,start[1]-7*pixelsize + 1)
            img.put("white", to=(end[0],end[1],start[0]-2*pixelsize+1,start[1]-2*pixelsize+1))
            #black 3x3
            end = (start[0]-6*pixelsize + 1,start[1]-6*pixelsize + 1)
            img.put("black", to=(end[0],end[1],start[0]-3*pixelsize+1,start[1]-3*pixelsize+1))

    ## -- Placing module matrix, set up limit
    limit = []
    border = (5 * pixelsize - 1, canvasscale - 4 * pixelsize - 1,11 * pixelsize - 1) # Up, down y, the dot right before the quiet zone and vertical timing's x value
    startingdot = (canvasscale - 4*pixelsize - 1,canvasscale - 4*pixelsize - 1)
    thatonedot = (13*pixelsize - 1, canvasscale - 11 * pixelsize - 1)
    timingstrips = 1 + version*4
    
    # place seps (range(10) due to masking and shit)
    for i in range(len(separators)):
        draw("separator", separators[i])
        for m in range(10):
            for n in range(10):
                limit.append((separators[i][0]-(m-1)*pixelsize,separators[i][1]-(n-1)*pixelsize))
    
    # place aligns
    for i in range(len(align)):
        draw("align", align[i])
        for m in range(5):
            for n in range(5):
                limit.append((align[i][0]-m*pixelsize,align[i][1]-n*pixelsize))

    # place timing strips
    for i in range(timingstrips):
        if i % 2 == 0:
            draw("dot",(11 * pixelsize - 1,canvasscale - (12 + i) * pixelsize - 1))
            draw("dot",((13 + i) * pixelsize - 1,11 * pixelsize - 1))
        limit.append((11 * pixelsize - 1,canvasscale - (12 + i) * pixelsize - 1))
        limit.append(((13 + i) * pixelsize - 1,11 * pixelsize - 1))
    
    # place version information (if version is 7 or higher)
    if version >= 7:
        binver = bin(version)[2:]
        binver = "0" * (6 - len(binver)) + binver
        verdivend = str(int(binver + "0" * 12))
        verdivsor = "1111100100101"
        while len(verdivend) > 12:
            verdiv = verdivsor + "0" * (len(verdivend)-len(verdivsor))
            verdivend = bin(int(verdivend,2)^int(verdiv,2))[2:]
        verdivend = "0" * (12 - len(verdivend)) + verdivend
        binver += verdivend
        binver = list(binver)
        binver.reverse()
        for x in range(3):
            for y in range(6):
                for i in range(18):
                    if binver[i] == "0":
                        draw("dot",(canvasscale - (14-x) * pixelsize - 1, (5+y) * pixelsize - 1))
                    limit.append((canvasscale - (14-x) * pixelsize - 1, (5+y) * pixelsize - 1))
        for x in range(6):
            for y in range(3):
                for i in range(18):
                    if binver[i] == "0":
                        draw("dot",((5+x) * canvasscale - 1, canvasscale - (14-y) * pixelsize - 1))
                    limit.append(((5+x) * canvasscale - 1, canvasscale - (14-y) * pixelsize - 1))

    # place that one dot (dark module)
    draw("dot",thatonedot)

    ## -- Placing data bits
    bits = list(data)
    current = startingdot
    ##print("DRAWING BITS")
    points = []
    while len(bits) != 0:
        step = 0
        dir = "up"
        while (dir == "up" and current[1] != border[0] and len(bits) != 0) or (dir == "up" and current[1] == border[0] and step % 2 != 1 and len(bits) != 0):
            if current not in limit:
                #print(current,dir,step)
                if bits[0] == "1":
                    draw("dot",current)
                points.append(((current),bits[0]))
                bits.pop(0)
            else:
                #print(current,dir,step,"limit hit")
                pass
            if step % 2 == 0:
                current = (current[0]-pixelsize,current[1])
            else:
                current = (current[0]+pixelsize,current[1]-pixelsize)
            step += 1
        
        # If border reached, reset step, move pointer to the left
        if current not in limit:
            #print(current, "turn")
            if len(bits) != 0:
                if bits[0] == "1":
                    draw("dot",current)
                points.append(((current),bits[0]))
                bits.pop(0)
        step = 0
        dir = "down"
        current = (current[0] - pixelsize, current[1])
        if current[0] == border[2]:
            current = (current[0] - pixelsize, current[1])
        while (dir == "down" and current[1] != border[1] and len(bits) != 0) or (dir == "down" and current[1] == border[1] and step % 2 != 1 and len(bits) != 0):
            if current not in limit:
                #print(current,dir,step)
                if bits[0] == "1":
                    draw("dot",current)
                points.append(((current),bits[0]))
                    ##print(current)
                bits.pop(0)
            else:
                #print(current,dir,step,"limit hit")
                pass
            if step % 2 == 0:
                current = (current[0]-pixelsize,current[1])
            else:
                current = (current[0]+pixelsize,current[1]+pixelsize)
            step += 1
        if current not in limit:
            #print(current, "turn")
            if len(bits) != 0:
                if bits[0] == "1":
                    draw("dot",current)
                points.append(((current),bits[0]))
                bits.pop(0)
        current = (current[0] - pixelsize, current[1])
    
    ## -- MASKING & FORMAT
    ecc = "10"
    mask = "010"
    dividend = str(int(ecc + mask + "0"*10)) #combine, add 10 0s and remove left side 0s
    divisor = "10100110111"
    while len(dividend) > 10: # XOR that shi until its 10 numbers 
        paddiv = divisor + "0" * (len(dividend) - len(divisor))
        dividend = bin(int(dividend,2)^int(paddiv,2))[2:]
    if len(dividend) < 10: # pad it on the left if it refuses to be 10 numbers
        dividend = "0"*(10 - len(dividend)) + dividend
    formatstr = ecc + mask + dividend
    formatstr = bin(int(formatstr,2)^int("101010000010010",2))[2:] #XOR with a certain binary
    formatstr = "0" * (15 - len(formatstr)) + formatstr # Restore some might've been lost 0s
    print(formatstr)
    # 001110011100111
    
    # Draw it out on the QR code
    for i in range(7):
        if formatstr[i] == "1":
            if i == 6:
                draw("dot",(12*pixelsize - 1,13*pixelsize - 1))
            else:
                draw("dot",((5+i)*pixelsize - 1,13*pixelsize - 1))
            draw("dot",(13*pixelsize-1,canvasscale - (4+i)*pixelsize - 1))
    for i in range(7,15):
        if formatstr[i] == "1":
            if i >= 9:
                draw("dot",(13*pixelsize - 1,(19-i)*pixelsize - 1))
            else:
                draw("dot",(13*pixelsize - 1,(20-i)*pixelsize - 1))
            draw("dot",(canvasscale - (18-i)*pixelsize - 1,13*pixelsize - 1))

    # Apply the masking
    def flip(start,bit):
        end = (start[0] - pixelsize + 1,start[1] -pixelsize + 1)
        if bit == "1": # black -> white
            color = "white"
        else:
            color = "black"
        img.put(color, to=(end[0],end[1],start[0]+1,start[1]+1))
    
    flip_targets = []
    for pos in points:
        if (((pos[0][0] + 1) // pixelsize) - 5) % 3 == 0:
            flip_targets.append(pos)
    
    for point in flip_targets:
        flip(point[0],point[1])
    
    # Saving the image
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_folder = os.path.join(script_dir, "Output")
    file_path = os.path.join(target_folder, f"{name}.png")

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    request = input("Save image in Output? [y/n]: ")
    while request != "y" and request != "n":
        request = input("Save image in Output? [y/n]: ")
    if request == "n":
        print("File discarded")
    else:
        img.write(file_path,format="png")
        print(f"File saved to: {file_path}")
    root.destroy()