from algorithm import hanoi_solver

for n in (1, 2, 3):
    print(f"--- {n} disk(s) ---")
    print(hanoi_solver(n))
    print()
