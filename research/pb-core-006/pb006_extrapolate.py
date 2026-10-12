import mpmath as mp

mp.mp.dps = 40

data = [
    (10**3, mp.mpf('10'),        mp.mpf('-0.37524736921101')),
    (10**4, mp.mpf('21.544347'), mp.mpf('-0.36680087639884')),
    (10**5, mp.mpf('46.415888'), mp.mpf('-0.36287406308367')),
    (10**6, mp.mpf('100'),       mp.mpf('-0.36104845951752')),
]

a = mp.pi * mp.sqrt(mp.mpf(2) / 3)
x_star = (a / 2) ** (mp.mpf(2) / 3)
D = (x_star / 12
     - 5 / (72 * x_star ** 2)
     - (a / 48 + 1 / a) / mp.sqrt(x_star))
E_log = (2 * x_star ** 9 - 75 * x_star ** 3 - 550) / (2160 * x_star ** 4)

print(f"Symbolic D     = {mp.nstr(D, 20)}")
print(f"Symbolic E_log = {mp.nstr(E_log, 20)}")
print()

ys = [(t, t * (tD - D)) for (_, t, tD) in data]
for (_, t, tD), (_, y) in zip(data, ys):
    print(f"t = {mp.nstr(t, 10):>10}   t*(t*Delta_n - D) = {mp.nstr(y, 16)}")

(t1, y1), (t2, y2), (t3, y3) = ys[1], ys[2], ys[3]
M = mp.matrix([
    [1, 1 / t1, 1 / t1 ** 2],
    [1, 1 / t2, 1 / t2 ** 2],
    [1, 1 / t3, 1 / t3 ** 2],
])
b = mp.matrix([y1, y2, y3])
sol = mp.lu_solve(M, b)
E_fit, F_fit, G_fit = sol[0], sol[1], sol[2]

print()
print("3-point Richardson fit (n = 1e4, 1e5, 1e6):")
print(f"  E_log (fit)   = {mp.nstr(E_fit, 16)}")
print(f"  E_log (exact) = {mp.nstr(E_log, 16)}")
print(f"  |gap|         = {mp.nstr(abs(E_fit - E_log), 6)}")
print(f"  F (fit)       = {mp.nstr(F_fit, 12)}")
print(f"  G (fit)       = {mp.nstr(G_fit, 12)}")
