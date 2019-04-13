
def reduce_routes(mapdata):
    i = 0
    for line in mapdata:
        i += 1
        if i > 2:
            if '1. ' in line:
                line = line[3:]
            print(line, end='')
        if line.isspace():
            break

#example: l = reduce_routes('mapdata.txt')
