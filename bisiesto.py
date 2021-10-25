#definir si un año es bisiesto con unas cokndiciones dadas

def is_leap(year):
    leap = False
    if(year%4==0):
        if(year%100==0):
            leap=False
        if(year%400==0):
            leap=True
    else:
        leap=False

    return leap

is_leap(year)

year = int(input())
print(is_leap(year))