#The statement below creates a function which can be called later using cal_mean()
def cal_mean():
    #The statement below creates a list which can add or minus stuff from it.
    numbers = []
    #This creates a while loop which will only end if the user want it to end.
    while True:
        print("Enter the number to add it to the calculator")
        print("Enter 0 to finish")
        print("1 to calculate the mean")
        print("2 to calculate the median")
        print("3 to calculate the mode")
        #This creates a numeric variable which the user can put integers(numbers) into
        num = int(input(": "))
        #The code below means that if the user puts nothing it will inform the user to put integers.
        if num == "":
            print("Please enter a number.")
        #The code below means that if the user puts 0 it ends the program.
        elif num == 0:
            print("bye <---------------------------")
            break
        #The code below means that if user enter 1 it will calculate the mean of all the numbers that the user have previously input
        elif num == 1:
            mean = sum(numbers)/len(numbers)
            print("The mean is: ", mean, "<---------------------------")
        #The code below will calculate and print out the median of the number from the list of numbers the user have put it.
        elif num == 2:
            median = sorted(numbers) [len(numbers) // 2]
            print("The median is: ", median, "<---------------------------")
        #The code below will caculate the mode and print out the mode from the list of numbers user have input in.
        elif num == 3:
            mode = max(numbers, key = numbers.count)
            print("The mode is: ", mode, "<---------------------------")
        #This code means that if the user doesn't input anything from the above code it will add that number to the list name (num)
        else:
            numbers.append(num)
            print("Successfully added!")
            print(numbers)
#This code make it into a function which can be called later using cal()
def cal():
    #This is a function inside a function which can be call using add(num1, num2)
   def add(x, y):
      return x + y
   def subtract(x, y):
      return x - y
   def multiply(x, y):
      return x * y
   def divide(x, y):
      return x / y

   while True:
      print("Select operation.")
      print("1.Add")
      print("2.Subtract")
      print("3.Multiply")
      print("4.Divide")
      print("0.End")
      choice = input("Enter choice(1/2/3/4/0): ")
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      if choice == '1':
         print(num1,"+",num2,"=", add(num1,num2))
      elif choice == '2':
         print(num1,"-",num2,"=", subtract(num1,num2))
      elif choice == '3':
         print(num1,"*",num2,"=", multiply(num1,num2))
      elif choice == '4':
         print(num1,"/",num2,"=", divide(num1,num2))
      elif choice == '0':
         break
      else:
         print("Invalid input")

print("This is a simple calculator")
print("1 is a mean, mode, median, calculator")
print("2 is a simple calculator")
print("0 to end")
user_choice = int(input("Please enter a number?: "))
while True:
    if user_choice == 1:
        cal_mean()
    elif user_choice == 2:
        cal()
    elif user_choice == 0:
        break
    else:
        print("Invalid answer")