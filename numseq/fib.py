def fib(n):
    """fib(n): returns nth number of fibbonacci sequence"""
    seq = [0, 1]
    for _ in range(n-1):
        seq.append(seq[-1] + seq[-2])
    return seq[n]
