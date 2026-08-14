def deneraPares(limite):

    num = 1

    while num < limite:

        yield num*2
        num += 1 


devuelvePares = deneraPares(10)

print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))

print("Aqui podria ir mas codigo...")

print(next(devuelvePares))