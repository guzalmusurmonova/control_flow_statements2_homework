def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    z=a
    if z>b:
        z=b
    if z>c:
        z=c
    
    return z
a=int(input())
b=int(input())
c=int(input())
print(main(a,b,c))