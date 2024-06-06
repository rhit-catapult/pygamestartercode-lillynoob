# Program Header

def main():
    # Lilly Bailey
    print("Python Syntax Guide!")
    variables()
    strings()
    loops()
    sequences()

def variables():
    print("- - - Variables - - -")
    x = 7 #Integer
    b = "Bob" #String
    p = 8.4 #Float

    print(x+3)
    print(b*3)
    print(type(x))
    print(type(b))
    print(type(p))

def strings():
    print("- - - Strings - - -")

    str1 = "Can't" #Using double quotes
    str2 = 'Dave' #Using single quotes
    str3 = """I can use ' or " or even 
more lines!""" #TRIPLE QUOTESSS

    print(str1)
    print(str2)
    print(str3)

    x = 42
    str4 = f"X equals {x}. Fun." #Format string, {} makes variables return values

    print(x)

    print(str4)

def loops():
    print("- - - Loops - - -")
    x = 0
    while True:
        x += 1
        print(f"Now it is {x}!")
        if x > 4:
            break
    print(x)

    print("- For i in Range -")

    total = 1
    for k in range(1, 101):
        total *= k
    print(total)

def sequences():
    print("- - - Sequences - - -")
    my_list = [4, 5, 6, 7]
    print(my_list)
    my_list[2] = 99
    print(my_list)

    my_list.append(1000)
    print(my_list)
    my_list.
    my_list.pop()
    print(my_list)
    my_list.
    my_list.sort()
    print(my_list)

    print(f"The length of this list is {len(my_list)}!")

    for k in range(len(my_list)):
        my_list[k] += 10
    print(my_list)

    product = 1
    for k in range(len(my_list)):
        product *= my_list[k]
    print(product)

main()