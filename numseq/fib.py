def fib(n):
    seq = [0, 1]
    for _ in range(n-1):
        seq.append(seq[-1] + seq[-2])
    return seq[n]