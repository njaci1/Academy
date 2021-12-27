

def fib_series_gen(n):
    init = [0, 1]
    count = len(init)

    while count < n:
        nex_num_in_series = init[-1] + init[-2]

        init.append(nex_num_in_series)

        count = count + 1

    return init

print(fib_series_gen(5))