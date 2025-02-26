for Number in range(1,101):
    if Number %3==0:
        if Number %5==0:
            print("FizzBuzz")
        else:
            print("Fizz")

    elif Number %5==0:
        print("Buzz")


    else:
        print(Number)
