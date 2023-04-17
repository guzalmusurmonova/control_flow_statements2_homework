def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    z=a 
    if z<b:
        z=b
    if z<c:
        z=c
    y=a
    if y>b:
        y=b
    if y>c:
        y=c
    f=a
    if y==f or f==z:
        f==b 
    if y==f or f==z:
        f==c

        
    return f
a=int(input())
b=int(input())
c=int(input())
print(main(a,b,c))