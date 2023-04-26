def summa(x):
    if len(x) == 1:
        return sum(x)
    elif x == []:
        return 0
    else:
        return x[0] + summa(x[1:])
      
if __name__ == '__main__':
    array = [10,20,30,40,50]
    print(summa(array))
