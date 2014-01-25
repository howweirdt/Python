#current letter/number key- 0 = blank 1 = path w = wall c = corner
import random
pos = [0,0]
prox = []
overallcount = 0
randscale = 2
count = 0
linecount = 0
xcount = 0
choose = 0
overallcount = 0
extracount = 0
old = [[0,0]]
extra = [[0,0]]                 #blank grid
text = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
xlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,17,18,19,30,31,32,33,34,35,36]
line1 = []          #list where usable path positions will be stored in order
line1wall = ['w','w','w','w','w','w','w','w','w','w']
line2 = []
line2wall = ['w','w','w','w','w','w','w','w','w','w']
line3 = []
line3wall = ['w','w','w','w','w','w','w','w','w','w']
line4 = []
line4wall = ['w','w','w','w','w','w','w','w','w','w']
line5 = []
line5wall = ['w','w','w','w','w','w','w','w','w','w']
line6 = []
line6wall = ['w','w','w','w','w','w','w','w','w','w']
line7 = []
line7wall = ['w','w','w','w','w','w','w','w','w','w']
line8 = []
line8wall = ['w','w','w','w','w','w','w','w','w','w']
line9 = []
line9wall = ['w','w','w','w','w','w','w','w','w','w']
line10 = []
line10wall = ['w','w','w','w','w','w','w','w','w','w']
pathnumber = 0
currentpath = 0
directionindex = [] #list of directions to be used later to determine wall orrentation

def new(): #main path generator
    global pos
    global last
    global old
    global prox
    global randscale
    global overallcount
    global directionindex
    overallcount += 1
    
    if random.randint(0,1) == 0: #generates an increase or decrease in the x or y
        if random.randint(0,randscale) != 0:
            if pos[0] < 9 and [pos[0]+1,pos[1]] not in old:
                pos[0] += 1
                print pos
                old.append([pos[0],pos[1]])
                directionindex.append('right')
            else:
                if overallcount < 400:
                    new()
        else:
            if pos[0] > 0 and [pos[0]-1,pos[1]] not in old:
                pos[0] -= 1
                print pos
                old.append([pos[0],pos[1]])
                directionindex.append('left')
            else:
                if overallcount < 400:
                    new()
    else:
        if random.randint(0,randscale) != 0:
            if pos[1] < 9 and [pos[0],pos[1]+1] not in old:
                pos[1] += 1
                print pos
                old.append([pos[0],pos[1]])
                directionindex.append('down')
            else:
                if overallcount < 400:
                    new()
        else:
            if pos[1] > 0 and [pos[0],pos[1]-1] not in old:
                pos[1] -= 1
                print pos
                old.append([pos[0],pos[1]])
                directionindex.append('up')
            else:
                if overallcount < 400:
                    new()

while count < 20: #calls path generation
    new()
    count += 1
    current = [pos[0],pos[1]]
    xlist[count-1] = current[1]*10+current[0] #converts coordinates to position in array
    
def log(): #formats information so it can be written to file
    global xcount
    global linecount
    while xcount < 35: #sets the path values on the array
        xcount += 1
        text[xlist[xcount-1]] = '1'
    if len(extra) > 1:
        text[xlist[len(extra)+18]] = '2'
    else:
        logchoose = random.randint(0,19)
        text[xlist[logchoose]] = '2'
    text[xlist[len(old)-2]] = '3'

    while linecount < 10: #converts array to lines
        linecount += 1
        line1.append(text[linecount-1])
        line2.append(text[linecount-1+10])
        line3.append(text[linecount-1+20])
        line4.append(text[linecount-1+30])
        line5.append(text[linecount-1+40])
        line6.append(text[linecount-1+50])
        line7.append(text[linecount-1+60])
        line8.append(text[linecount-1+70])
        line9.append(text[linecount-1+80])
        line10.append(text[linecount-1+90])

def write(): #writes data to file
    global grid
    lines = [' w '.join(line1),' c '.join(line1wall),' w '.join(line2),' c '.join(line2wall),' w '.join(line3),' c '.join(line3wall),' w '.join(line4),' c '.join(line4wall),' w '.join(line5),' c '.join(line5wall),' w '.join(line6),' c '.join(line6wall),' w '.join(line7),' c '.join(line7wall),' w '.join(line8),' c '.join(line8wall),' w '.join(line9),' c '.join(line9wall),' w '.join(line10),' c '.join(line10wall)]
    grid = '\n\n'.join(lines)
    charfile = open("level.txt","w")
    charfile.write(grid)
    charfile.close()
    print grid

def randpoint(): #generates a random point on main path for branching paths
    choose = random.choice(old)
    pos = [choose[0],choose[1]]
    epaths()
        
def newe(): #extra path generator
    global pos
    global last
    global extra
    global prox
    global randscale
    global overallcount
    global pathnumber
    global directionindex
    overallcount += 1
    
    if random.randint(0,1) == 0: #generates an increase or decrease in the x or y
        if random.randint(0,randscale) != 0:
            if pos[0] < 9 and [pos[0]+1,pos[1]] not in old and [pos[0]+1,pos[1]] not in extra:
                pos[0] += 1
                print str(pos) + 'e'
                extra.append([pos[0],pos[1]])
                directionindex.append('right')
            else:
                if overallcount < 400:
                    newe()
        else:
            if pos[0] > 0 and [pos[0]-1,pos[1]] not in old and [pos[0]-1,pos[1]] not in extra:
                pos[0] -= 1
                print str(pos) + 'e'
                extra.append([pos[0],pos[1]])
                directionindex.append('left')
            else:
                if overallcount < 400:
                    newe()
    else:
        if random.randint(0,randscale) != 0:
            if pos[1] < 9 and [pos[0],pos[1]+1] not in old and [pos[0],pos[1]+1] not in extra:
                pos[1] += 1
                print str(pos) + 'e'
                extra.append([pos[0],pos[1]])
                directionindex.append('down')
            else:
                if overallcount < 400:
                    newe()
        else:
            if pos[1] > 0 and [pos[0],pos[1]-1] not in old and [pos[0],pos[1]-1] not in extra:
                pos[1] -= 1
                print str(pos) + 'e'
                extra.append([pos[0],pos[1]])
                directionindex.append('up')
            else:
                if overallcount < 400:
                    newe()



def epaths(): #controls extra path generation
    global pos
    global extracount
    global currentpath
    global pathnumber
    global directionindex
    if currentpath < pathnumber:
        currentpath += 1
        epaths()
        directionindex.append(' ')
        while extracount < 5:
            extracount += 1
            newe()
            current = [pos[0], pos[1]]
            xlist[currentpath*5+extracount+14] = current[1]*10+current[0]
        randpoint()

def enumber(): #determines number of extra paths being generated
    global choose
    global pos
    global pathnumber
    global currentpath
    pathnumber = random.randint(1,3)
    currentpath = 0
    print pathnumber
    epaths()
    
if count == 20: #calls functions in order
    choose = random.choice(old)
    pos = [choose[0],choose[1]]
    enumber()
    if extracount == 5:
        print directionindex
        log()
        if linecount == 10:
            write()
            
