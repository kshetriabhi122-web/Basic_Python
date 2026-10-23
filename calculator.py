print("Welcome To This Basic Python Project")
print("This Is A Program To Perform Basic Calculations ")
Readiness = input("Are You Ready ? (yes/no): ").strip().lower()
if Readiness =="yes":
    print("Enter The Numbers That You Want to Perform Basic Calculations on")
    num1 = (float(input("Enter The Number")))
    num2 = (float(input("Enter The Number")))
    print("What Do You Want to Perform ?")
    print("Options: Addition, Subtraction, Multiply, Division")
    operation = input("Enter operation: ").strip().lower()
    
    
    if operation == "addition" or operation == "add":
        result = num1 + num2
        print(f"The result of addition is: {result}")
        
    elif operation == "subtraction" or operation == "subtract":
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
        
    elif operation == "multiply" or operation == "multiplication":
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
        
    elif operation == "division" or operation == "divide":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error: Cannot divide by zero!")
            
    else:
        print("Invalid operation selected.")
else:
    print("Goodbye! Run the program again when you are ready.")
