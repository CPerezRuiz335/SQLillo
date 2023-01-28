def strategy(mapa, worker, memory):
    for w in range(8):
        r = randint(0, 3)
        match r:
            case 0:
                worker[w].move_up()
            case 1:
                worker[w].move_down()
            case 2:
                worker[w].move_left()
            case 3:
                worker[w].move_right()