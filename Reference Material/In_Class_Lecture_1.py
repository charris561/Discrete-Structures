#class example 11/2/22

def sumEven(a,b):
    return (a+b) % 2 == 0

def checkTransitive(relation):
    for a in range(0,100):
        for b in range (0, 100):
            for c in range (0, 100):
                #look for counterexamples
                if relation(a,b) and relation(b,c):
                    if relation(a,c):
                        #if here, no counter example
                        pass
                    else:
                        #if here, found counter example
                        return(a,b,c)

    return -1

print(checkTransitive(sumEven))