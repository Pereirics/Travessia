def build(mapa):
    adj = {}
    y = 0
    for linha in mapa:
        x = 0
        for ponto in linha:
            if ponto not in adj:
                if x+1 < len(linha):
                    if abs(int(mapa[y][x+1]) - int(ponto)) <= 2:
                        adj[(x, y)] = {(x+1, y): abs(int(mapa[y][x+1]) - int(ponto)) + 1}
                        adj[(x+1, y)] = {(x, y): abs(int(mapa[y][x+1]) - int(ponto)) + 1}
                if x-1 >= 0:
                    if abs(int(mapa[y][x-1]) - int(ponto)) <= 2:
                        adj[(x, y)] = {(x-1, y): abs(int(mapa[y][x-1]) - int(ponto)) + 1}
                        adj[(x-1, y)] = {(x, y): abs(int(mapa[y][x-1]) - int(ponto)) + 1}
                if y+1 < len(mapa):
                    if abs(int(mapa[y+1][x]) - int(ponto)) <= 2:
                        adj[(x, y)] = {(x, y+1): abs(int(mapa[y+1][x]) - int(ponto)) + 1}
                        adj[(x, y+1)] = {(x, y): abs(int(mapa[y+1][x]) - int(ponto)) + 1}
                if y-1 >= 0:
                    if abs(int(mapa[y-1][x]) - int(ponto)) <= 2:
                        adj[(x, y)] = {(x, y-1): abs(int(mapa[y-1][x]) - int(ponto)) + 1}
                        adj[(x, y-1)] = {(x, y): abs(int(mapa[y-1][x]) - int(ponto)) + 1}
            else:
                if x+1 < len(linha):
                    if abs(int(mapa[y][x+1]) - int(ponto)) <= 2:
                        adj[(x, y)][(x+1, y)] = abs(int(mapa[y][x+1]) - int(ponto)) + 1
                        if (x+1, y) not in adj:
                            adj[(x+1, y)] = {(x, y): abs(int(mapa[y][x+1]) - int(ponto)) + 1}
                        else:
                            adj[(x+1, y)][(x, y)] = abs(int(mapa[y][x+1]) - int(ponto)) + 1
                if x-1 >= 0:
                    if abs(int(mapa[y][x-1]) - int(ponto)) <= 2:
                        adj[(x, y)][(x-1, y)] = abs(int(mapa[y][x-1]) - int(ponto)) + 1
                        adj[(x-1, y)][(x, y)] = abs(int(mapa[y][x-1]) - int(ponto)) + 1
                if y+1 < len(mapa):
                    if abs(int(mapa[y+1][x]) - int(ponto)) <= 2:
                        adj[(x, y)][(x, y+1)] = abs(int(mapa[y+1][x]) - int(ponto)) + 1
                        if (x, y+1) not in adj:
                            adj[(x, y+1)] = {(x, y): abs(int(mapa[y+1][x]) - int(ponto)) + 1}
                        else:
                            adj[(x, y+1)][(x, y)] = abs(int(mapa[y+1][x]) - int(ponto)) + 1
                if y-1 >= 0:
                    if abs(int(mapa[y-1][x]) - int(ponto)) <= 2:
                        adj[(x, y)][(x, y-1)] = abs(int(mapa[y-1][x]) - int(ponto)) + 1
                        adj[(x, y-1)][(x, y)] = abs(int(mapa[y-1][x]) - int(ponto)) + 1
            x += 1
        y += 1
    return adj


def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist


def travessia(mapa):
    adj = build(mapa)
    adj = fw(adj)
    menor = 1000
    for o in adj:
        if o[1] == 0:
            for d in adj[o]:
                if d[1] == len(mapa)-1:
                    if adj[o][d] < menor:
                        ponto = o
                        menor = adj[o][d]
    result = (ponto[0], menor)
    return result


mapa = ["90999",
        "00000",
        "92909",
        "94909"]

print(travessia(mapa))

