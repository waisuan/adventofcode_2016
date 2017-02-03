def isInteger(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

file = open('files/aoc_day23.txt', 'r')
dict = {'a': 12}
instr = []
for line in file:
    line = line.split()
    instr.append(line)
idx = 0
while 1:
    #print ('idx : ' + str(idx))
    if idx >= len(instr) or idx < 0:
        break
    if idx == 4:
        dict['a'] = dict['b'] * dict['d']
        dict['c'] = 0
        dict['d'] = 0
        idx = 10
    i = instr[idx]
    #print (i)
    if i[0] == 'cpy':
        x = 0
        if isInteger(i[1]):
            x = int(i[1])
        else:
            x = dict[i[1]]
        if not isInteger(i[2]):
            dict[i[2]] = x
    elif i[0] == 'inc':
        if i[1] in dict:
            dict[i[1]] = dict[i[1]] + 1
    elif i[0] == 'dec':
        if i[1] in dict:
            dict[i[1]] = dict[i[1]] - 1
    elif i[0] == 'jnz':
        # x/y could be char or num
        x = 0
        if isInteger(i[1]):
            x = int(i[1])
        else:
            x = dict[i[1]]
        y = 0
        if isInteger(i[2]):
            y = int(i[2])
        else:
            y = dict[i[2]]
        if x != 0:
            #print ('jump to : ' + str(y))
            idx += y
            continue
    elif i[0] == 'tgl':
        away = idx + dict[i[1]]
        if away > 0 and away < len(instr):
            if instr[away][0] == 'inc':
                instr[away][0] = 'dec'
            elif instr[away][0] == 'dec':
                instr[away][0] = 'inc'
            elif instr[away][0] == 'cpy':
                instr[away][0] = 'jnz'
            elif instr[away][0] == 'jnz':
                instr[away][0] = 'cpy'
            elif instr[away][0] == 'tgl':
                instr[away][0] = 'inc'
    idx += 1
file.close()
print (dict['a'])
