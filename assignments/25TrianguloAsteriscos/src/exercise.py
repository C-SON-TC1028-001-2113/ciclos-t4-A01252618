
def main():
    #escribe tu código abajo de esta línea
    n = int(input("Enter triangle height: "))
    for i in range(1,n+1):
        print(' '*(n-i)+ '*'*i)


if __name__=='__main__':
    main()
