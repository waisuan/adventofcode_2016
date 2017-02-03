
file = open('files/aoc_day22.txt', 'r')
file.readline()
file.readline()
allNodes = []
for line in file:
    line = line.split()
    #print(line)
    allNodes.append(line)
pairs = 0
for node1 in allNodes:
    nodeTokens1 = node1[0].split('-')
    x1 = nodeTokens1[-2]
    y1 = nodeTokens1[-1]
    if int(node1[2][:-1]) == 0:
        continue
    for node2 in allNodes:
        nodeTokens2 = node2[0].split('-')
        x2 = nodeTokens2[-2]
        y2 = nodeTokens2[-1]
        if x1 == x2 and y1 == y2:
            continue
        if int(node1[2][:-1]) <= int(node2[3][:-1]):
            pairs+=1
file.close()
print (pairs)
