
def p(n):
    if n<0:
        return False
    else:
        c=str(n)
        b=c[::-1]
        print(b)
        if c==b:
            return True
        else:
            return False
print(p(121))

