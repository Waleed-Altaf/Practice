
try:
    num1 = float(input("enter number 1:" ))
    num2 = float(input("enter number 2:"))
    operator = input("enter operator(+,-,*,%)")

    if operator == '+':
        result = num1 + num2
        print("result" , result)   
    elif operator == '-':
        result = num1 - num2
        print("result" , result)
    elif operator == '*':
        result = num1 * num2
        print("result" , result)
    else:
        print("invalid operator")
except ValueError:
    print("Invalid input! Please enter numeric values.")
except Exception as e:
    print("An error occurred:", e)
 
