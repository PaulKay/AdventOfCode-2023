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

nSeeds = len(seeds)
seeds_new = []
seeds_range = []
for i in range(nSeeds):
    if i%2 == 0:
        seeds_new.append(int(seeds[i]))
    else:
        seeds_range.append(int(seeds[i]))
seeds = seeds_new
#print('Seed start',seeds_new)
#print('seed range',seeds_range)




'''
destinations = []
for seed,seed_range in zip(seeds,seeds_range):
    print('Seed',seed)
    sources = [seed]
    destinations_maps = []
    for map in maps:
        destinations_lines = []
        for source in sources:            
            for line in map:
                line0 = int(line[0])
                line1 = int(line[1])
                line2 = int(line[2])
                if source >= line1 and source <= line1 + line2:
                    destination = line0 + source - line1
                elif source < line1:
                    if line1 - source < seed_range:
                        destination = line0
                    else:
                        destination = source
                elif source > line1 + line2:
                    destination = source
                destinations_lines.append(destination)
        sources = destinations_lines
        destinations_maps.append(destinations_lines)
    
'''