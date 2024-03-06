import sys, random; from math import sqrt

def ADD_numbers(a,b):
  sum_ = a+b
  return sum_

def mul_numbers(c,d):
  product=c*d
  return product

def main():
    print("Welcome to the Calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result_sum = ADD_numbers(num1, num2)
    print("Sum:", result_sum)

    result_product = mul_numbers(num1, num2)
    print("Product:", result_product)

    sqrt_result = sqrt(result_sum)
    print("Square root of the sum:", sqrt_result)

    if result_product > 100:
        print("Product is greater than 100!")
    else:
        print("Product is not greater than 100.")

    sys.exit()

if __name__ == "__main__":
    main()
