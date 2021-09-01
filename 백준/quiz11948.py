a, b, c, d, e, f = map(int,input().split())

sci = {a, b, c, d}
soc = {e, f}

print(a + b + c + d - min(sci) + e + f - min(soc))

