import tkinter as tk
def output(version,data):
    ### PREPARING PROPERTIES
    # Version properties 
    properties = [0,0,[(6,18),10],[(6,22),10],[(6,26),10],[(6,30),10],[(6,34),10],[(6,22,38),10],[(6,24,42),10],[(6,26,46),10],[(6,28,50),10],[(6,30,54),10],[(6,32,58),10],[(6,34,62),10],[(6,26,46,66),10],[(6,26,48,70),10],[(6,26,50,74),10],[(6,30,54,78),10],[(6,30,56,82),10],[(6,30,58,86),10],[(6,34,62,90),10],[(6,28,50,72,94),5],[(6,26,50,74,98),5],[(6,30,54,78,102),5],[(6,28,54,80,106),5],[(6,32,58,84,110),5],[(6,30,58,86,114),5],[(6,34,62,90,118),5],[(6,26,50,74,98,122),5],[(6,30,54,78,102,126),5],[(6,26,52,78,104,130),5],[(6,30,56,82,108,134),5],[(6,34,60,86,112,138),5],[(6,30,58,86,114,142),5],[(6,34,62,90,118,146),5],[(6,30,54,78,102,126,150),5],[(6,24,50,76,102,128,154),5],[(6,28,54,80,106,132,158),5],[(6,32,58,84,110,136,162),5],[(6,26,54,82,110,138,166),5],[(6,30,58,86,114,142,170),5]]
    codesize = 17 + 4 * version
    fullsize = codesize + 8
    pixelsize = properties[version][1]
    canvasscale = pixelsize * fullsize
    nums = properties[version][0]
    align = []
    separators = []

    # Version 1 does not have alignment patterns
    if version > 1:
        for i in range(len(nums)):
            for g in range(len(nums)):
                # Exclusively avoids the separators
                if (i != 0 and g != 0) or (i != len(nums) - 1 and g != 0) or (i != len(nums) - 1 and g != len(nums) - 1):
                    align.append(((nums[i]+6)*pixelsize,(nums[g]+6)*pixelsize))

    # Separators, coords as bottom right dot (white dot)
    separators.append((8 * pixelsize - 1,8 * pixelsize - 1))
    separators.append(((fullsize - 2) * pixelsize - 1,8 * pixelsize - 1))
    separators.append((8 * pixelsize - 1,(fullsize - 2) * pixelsize - 1))

    ### PREPARING CANVAS
    ## -- Initialize canvas
    root = tk.Tk()
    canvas = tk.Canvas(root, width=canvasscale, height=canvasscale, bg="white")
    canvas.pack()

    img = tk.PhotoImage(width=canvasscale, height=canvasscale)
    canvas.create_image((canvasscale // 2, canvasscale // 2), image=img)
    ## -- Drawing function

    def draw(type, start): # "dot"/"align"/"separator" as type, (x,y) as starting point
        # takes starting point as bottom right pixel
        if type == "dot":
            end = (start[0]-pixelsize + 1,start[1]-pixelsize + 1)
            for x in range(end[0],start[0] + 1):
                for y in range(end[1],start[1] + 1):
                    img.put("black",(x,y))
        
        elif type == "align":
            #black 5x5
            end = (start[0]-5*pixelsize + 1,start[1]-5*pixelsize + 1)
            for x in range(end[0],start[0] + 1):
                for y in range(end[1],start[1] + 1):
                    img.put("black",(x,y))
            #white 3x3
            end = (start[0]-4*pixelsize + 1,start[1]-4*pixelsize + 1)
            for x in range(end[0],start[0] - pixelsize + 1):
                for y in range(end[1],start[1] - pixelsize + 1):
                    img.put("white",(x,y))
            #black center
            draw("dot",(start[0]-2*pixelsize,start[1]-2*pixelsize))
        
        elif type == "separator":
            #white 9x9 (ignore)
            #black 7x7
            end = (start[0]-8*pixelsize + 1,start[1]-8*pixelsize + 1)
            for x in range(end[0],start[0] - pixelsize + 1):
                for y in range(end[1],start[1] - pixelsize + 1):
                    img.put("black",(x,y))
            #white 5x5
            end = (start[0]-7*pixelsize + 1,start[1]-7*pixelsize + 1)
            for x in range(end[0],start[0] -2*pixelsize + 1):
                for y in range(end[1],start[1] -2*pixelsize + 1):
                    img.put("white",(x,y))
            #black 3x3
            end = (start[0]-6*pixelsize + 1,start[1]-6*pixelsize + 1)
            for x in range(end[0],start[0] - 3*pixelsize + 1):
                for y in range(end[1],start[1] - 3*pixelsize + 1):
                    img.put("black",(x,y))

    ## -- Placing module matrix, set up limit
    limit = []
    border = (5 * pixelsize - 1, canvasscale - 4 * pixelsize - 1) # Up, down y, the dot right before the quiet zone
    startingdot = (canvasscale - 4*pixelsize - 1,canvasscale - 4*pixelsize - 1)
    thatonedot = (12*pixelsize, canvasscale - 11 * pixelsize - 1)
    timingstrips = 1 + version*4
    
    # place seps
    for i in range(len(separators)):
        draw("separator", separators[i])
        for m in range(9):
            for n in range(9):
                limit.append((separators[i][0]-m*pixelsize,separators[i][1]-n*pixelsize))
    
    # place aligns
    for i in range(len(align)):
        draw("align", align[i])
        for m in range(5):
            for n in range(5):
                limit.append((align[i][0]-m*pixelsize,align[i][1]-n*pixelsize))

    # place timing strips
    for i in range(timingstrips):
        if i % 2 == 0:
            draw("dot",(10 * pixelsize - 1,canvasscale - (12 + i) * pixelsize - 1))
        limit.append((10 * pixelsize - 1,canvasscale - (12 + i) * pixelsize - 1))