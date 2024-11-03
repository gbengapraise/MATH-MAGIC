def is_armstrong(num):
    num_str = str(num)
    digits = len(num_str)

    sum = 0

    for i in num_str:
        sum = sum + (int(i) ** digits)

    return sum == num 

num = int(input("Enter a number: "))
result = is_armstrong(num)

if result:
    print(num, "is an arrmstrong number")
else:
    print("it is not an armstrong number")