
file = open('files/aoc_day22.txt', 'r')
file.readline()
file.readline()
max = 23 # 23
allNodes = []
for i in range(0, max+1):
    allNodes.append([])
count = 0
for line in file:
    line = line.split()
    #print(line)
    allNodes[count].append(line)
    count += 1
    if count > max:
        count = 0
for node in allNodes:
    for n in node:
        tokens = n[0].split('-')
        if int(n[2][:-1]) == 0:
            print ('_' + '/' + n[1][:-1], end="")
        elif int(n[2][:-1]) > 100:
            print ('|' + '/' + n[1][:-1], end="")
        else:
            print (n[2][:-1] + '/' + n[1][:-1], end="")
        print (" ", end="")
    print ("\n")

# Did this by hand :: https://www.reddit.com/r/adventofcode/comments/5jor9q/2016_day_22_solutions/

file.close()
