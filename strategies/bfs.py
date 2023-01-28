def strategy(mapa, worker, memory):
    # -------- INIT --------- #
    if 'init' in memory:
        memory['ticks'] += 1
    else:
        memory['init'] = True
        memory['ticks'] = 0
        memory['color'] = worker[0].color
        memory['prevCoords'] = [(w.x, w.y) for w in worker]
    # ----------------------- #
    
    def insideLimits(coords: Tuple[int, int]) -> bool:
        # Pre: coords is tuple
        x, y = coords
        return x >= 0 and x < 40 and y >= 0 and y < 40

    def adjacent(coords, color: Tuple[int, int, int] = ANY) -> List[Tuple[int,int]]:
        # Pre: coords is tuple
        x, y = coords
        moves = [(x + i, y + j) for i,j in VALIDMOVES]
        moves = list(filter(lambda pos: insideLimits(pos) and mapa[x, y] in color, moves))
        shuffle(moves)
        return moves

    def moveInDirection(w: Worker, x: int, y: int):
        # Pre: w is from class worker and x, y are integers insideLimits
        difx = abs(w.x - x)
        dify = abs(w.y - y)

        if difx > dify: # mover horizontal
            if w.x < x: w.move_right()
            else: w.move_left()

        else: # mover vertical
            if w.y > y: w.move_down()
            else: w.move_up()

    def moveRandomly(w: Worker):
        options = adjacent((w.x, w.y))
        if options: 
            shuffle(options)
        else: 
            return
        pos = options.pop()
        
        if (w.x, w.y + 1) == pos: w.move_up()
        if (w.x, w.y - 1) == pos: w.move_down()
        if (w.x + 1, w.y) == pos: w.move_right()
        if (w.x - 1, w.y) == pos: w.move_left()

    def isEnemy(x: int, y: int) -> bool:
        return mapa[x, y] != memory['color']
    
    def bfs(x: int, y: int, fun: Callable, distance = float('inf')): 
        # Find coordinates of any square that satisfies 
        # fun and it is within a range of distance
        q = deque(); q.append((x,y))
        visited = set()
        visited.add((x,y))
        dist = {(x, y): 0}
        
        while q:
            node = q.popleft()
            if dist[node] > distance: 
                # Useful if you want to limit search range
                return None, None
            
            for neighbor in adjacent(node):
                dist[neighbor] = dist[node] + 1
                nx, ny = neighbor
                
                if fun(nx, ny): 
                    return nx, ny
                
                if not neighbor in visited: 
                    visited.add(neighbor)
                    q.append(neighbor)
                    
        return None, None
    
    for i, w in enumerate(worker):
        if memory['ticks'] > 0 and memory['prevCoords'][i] == (w.x, w.y):
            moveRandomly(w)

        else:
            memory['prevCoords'][i] = (w.x, w.y)
            x, y = bfs(w.x, w.y, isEnemy) # BFS finds closest enemy
            if x is not None:
                moveInDirection(w, x, y)