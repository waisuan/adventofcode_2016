shortest = 999999999

def search(grid, y, x, path, count, max):
    global shortest
    if grid[y][x] == '#':
        return
    if grid[y][x] != '#' and grid[y][x] != '.':
        count += 1
    if count == max:
        if shortest > path:
            shortest = path
        return
    #grid[y][x] = '#'
    path += 1
    search(grid, y, x+1, path, count, max)
    search(grid, y, x-1, path, count, max)
    search(grid, y+1, x, path, count, max)
    search(grid, y-1, x, path, count, max)
    #grid[y][x] = '.'


file = open('files/test.txt', 'r')
#line = file.readline().strip()
gridWidth = 0
gridHeight = 0
# grid = []
# for c in line:
#     gridSize += 1
lines = []
for line in file:
    line = line.strip()
    if gridWidth == 0:
        for c in line:
            gridWidth += 1
    gridHeight += 1
    lines.append(line)
grid = [[lines[y][x] for x in range(gridWidth)] for y in range(gridHeight)]
#print (gridSize)
#print (grid[1])
numCount = 0
startY = 0
startX = 0
for y in range(gridHeight):
    for x in range(gridWidth):
        if grid[y][x] == '0':
            print (str(y)+', '+str(x))
            startY = y
            startX = x
            #break
        elif grid[y][x] != '#' and grid[y][x] != '.':
            #print (grid[y][x])
            numCount += 1
print (str(numCount))
search(grid, startY, startX, 0, 0, numCount)
print (shortest)
file.close()
