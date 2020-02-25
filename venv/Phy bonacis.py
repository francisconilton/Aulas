def fibo(ant0, ant1, c):
    c += 1
    ant2 = ant0 + ant1
    if c >= 5:
        return ant2
    else:
        fibo(ant1*3, ant2, c)


print(fibo(1,1,0))

### nao terminado