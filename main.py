i = int(input())

de = i//2
mod = i%2
bi = str(mod)
while de > 1:
    mod = de % 2
    de //= 2
    bi = str(mod) + bi
bi = '1' + bi
print(bi)
