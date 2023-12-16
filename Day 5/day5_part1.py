import re
f = open('almanac.txt')

maps = []
maps_ix = []
nMaps = 0

ix = -1
flag = -1
for i,line in enumerate(f):
    if i == 0:
        seeds = re.findall(r'\d+',line)
        #print(seeds)
    if line == '\n':        
        nMaps = nMaps + 1
        maps.append([])
        maps_ix.append([]) # for troubleshooting
        ix = ix + 1
        flag = i+2
    
    if i >= flag and flag != -1:
        mapLine = re.findall(r'\d+',line)
        maps[ix].append(mapLine)
        maps_ix[ix].append(i)

destinations = []
for i,seed in enumerate(seeds):
    print('Seed',seed)
    seed = int(seed)
    source = seed
    for map,map_ix in zip(maps,maps_ix):
        for line,line_ix in zip(map,map_ix):
            line0 = int(line[0])
            line1 = int(line[1])
            line2 = int(line[2])
            if source >= line1 and source <= line1 + line2:
                destination = line0 + source - line1            
                print('Line', line_ix, line, 'source', source, 'destination', destination)
                source = destination
                break
    destinations.append(destination)


print('Min destination', min(destinations))