str1 = input("Введите 1 строку\n")
str2 = input("Введите 2 строку\n")

def string_comparison(str1,str2):
    if str1==str2:
        result = 1
    elif len(str1)>len(str2):
        result = 2
    if ((str1!=str2) and str2=='learn'):
        result = 3
    return result


print( string_comparison(str1,str2))