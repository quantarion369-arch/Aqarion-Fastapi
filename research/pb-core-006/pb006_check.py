import mpmath as mp

mp.mp.dps = 40


def partition_numbers(N):
    p = [0] * (N + 1)
    p[0] = 1
    for m in range(1, N + 1):
        s = 0
        k = 1
        while True:
            g1 = k * (3 * k - 1) // 2
            if g1 > m:
                break
            sign = 1 if (k % 2) else -1
            s += sign * p[m - g1]
            g2 = k * (3 * k + 1) // 2
            if g2 <= m:
                s += sign * p[m - g2]
            k += 1
        p[m] = s
    return p


def constants():
    a = mp.pi * mp.sqrt(mp.mpf(2) / 3)
    x_star = (a / 2) ** (mp.mpf(2) / 3)
    C = mp.mpf(3) / 2 * x_star ** 2
    K = mp.sqrt(mp.pi) / 6 * mp.exp(-x_star ** 3 / 6)
    D = (x_star / 12
         - 5 / (72 * x_star ** 2)
         - (a / 48 + 1 / a) / mp.sqrt(x_star))
    return a, x_star, C, K, D


def main():
    targets = [10**3, 10**4, 10**5, 10**6]
    Nmax = max(int(5 * n ** (mp.mpf(2) / 3)) + 10 for n in targets) + 100
    print(f"Computing partition numbers up to {Nmax} ...")
    p = partition_numbers(Nmax)
    print("Done.\n")

    a, x_star, C, K, D = constants()
    print(f"a      = {mp.nstr(a, 20)}")
    print(f"x*     = {mp.nstr(x_star, 20)}")
    print(f"C      = {mp.nstr(C, 20)}")
    print(f"K      = {mp.nstr(K, 20)}")
    print(f"D      = {mp.nstr(D, 20)}")
    print()

    print(f"{'n':>9} | {'t':>8} | {'t*Delta_n':>14} | {'t*Delta_n - D':>16}")
    print("-" * 60)
    for n in targets:
        t = mp.cbrt(n)
        kmax = min(n, int(5 * n ** (mp.mpf(2) / 3)) + 10)
        log_fact = mp.loggamma(n + 1)
        log_n = mp.log(n)
        total = mp.mpf(0)
        for k in range(1, kmax + 1):
            log_term = log_fact - mp.loggamma(n - k + 1) - k * log_n
            total += mp.exp(log_term) * k * p[k]
        leading = C * t + mp.log(n) / 2 + mp.log(K)
        delta = mp.log(total) - leading
        scaled = t * delta
        print(f"{n:>9} | {mp.nstr(t, 8):>8} | {mp.nstr(scaled, 14):>14} | {mp.nstr(scaled - D, 16):>16}")


if __name__ == "__main__":
    main()
