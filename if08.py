def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    if number==1:
        s="monday"
    if number==2:
        s="tuesday"
    if number==3:
        s="wendnesday"
    if number==4:
        s="thursday"
    if number==5:
        s="friday"
    if number==6:
        s="saturday"
    if number==7:
        s="sunday"
    return s 
print(main(6))