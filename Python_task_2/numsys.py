num = int(input("Enter a positive integer with at least 3 digits: "))

if num<=0:
    print("Please enter a positive number.")
elif num<100:
     print("Please enter a number with at least 3 digits.")   
else:
     binary = bin(num)[2:]
     octal = oct(num)[2:]
     hexa = hex(num)[2:]   

     last_digit = num%10

     if num%2==0:
          result = "Even"
     else:
          result="Odd"

     print(f"Entered number is {num}")
     print(f"Binary number is {binary}")
     print(f"Octal number is {octal}")
     print(f"Hexadecimal number is {hexa}")
     print(f"Last digit of the number is {last_digit}")
     print(f"The given number is {result}")
            

