def toh(n,src,des,aux):
    if n<= 0:
        return
    toh(n-1,src,aux,des)
    print (src,"->",des)
    toh(n-1,aux,des,src)

def main():
    n = 3
    toh(n,'A','C','B')
    print(toh)
main()