"""""
print ("hellooooo")

 x = 1

    if x == 1:
        print ("x is 1")   
        x = x + x
        print(x)
        if x == 16:
            print ("x is 16")


    while x < 20:
        print ("x is less than 20")
        x = x + 1
        print(x)
        if x == 16:
            print ("x is 20")
            break
        else:
            x = x + x
"""""

x = 1
y = 2

while y > x:
    x = x * y * y
    print ("Now x is: ", x)
    y = y * 3
    print ("Now y is: ", y)
    if x > y:
        print ("x is winning over y, finish")
    else:
        print ("y is winning over x")