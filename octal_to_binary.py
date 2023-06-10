def oct_dec(o):
    i=0
    dec=0
    while o:
        dec=dec+(o%10)*pow(8,i)
        o//=10
        i+=1
    return dec
def dec_bin(d):
    i=1
    binary=0
    while d:
        binary=binary+(d%2)*i
        d//=2
        i*=10
    return binary
octal=int(input())
decimal=oct_dec(octal)
binary=dec_bin(decimal)
print(binary)