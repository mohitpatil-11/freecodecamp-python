def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    states = []

    def record():
        states.append(' '.join(str(rod) for rod in rods))

    def move(disks, source, target, spare):
        if disks == 0:
            return
        move(disks - 1, source, spare, target)
        rods[target].append(rods[source].pop())
        record()
        move(disks - 1, spare, target, source)

    record()
    move(n, 0, 2, 1)
    return '\n'.join(states)
