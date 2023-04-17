def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1=n%10
    x2=n%100//10
    x3=n%1000//100
    x4=n%10000//1000
    x5=n//100000
    z=x1
    if z<x2:
        z=x2
    if z<x3:
        z=x3
    if z<x4:
        z=x4
    if z<x5:
        z=x5

    return z 
print(main(23546))