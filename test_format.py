import sys, random; from math import pow as p

def add_nums(a,b):
    result=a+b
    return result

def multiply_numbers(c,d):
    prod=c*d
    return prod

def main():
    print("Welcome to the Calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    sum_result = add_nums(num1, num2)
    print("Sum:", sum_result)

    product_result = multiply_numbers(num1, num2)
    print("Product:", product_result)

    power_result = p(sum_result, 2)
    print("Square of the sum:", power_result)

    if product_result > 100:
        print("Product is greater than 100!")
    else:
        print("Product is not greater than 100.")

    sys.exit()

if __name__ == "__main__":
    main()
