def cal_mean():
    numbers = []
    while True:
        print("Enter the number to add it to the calculator")
        print("Enter 0 to finish")
        print("1 to calculate the mean")
        print("2 to calculate the median")
        print("3 to calculate the mode")
        num = int(input(": "))
        if num == "":
            print("Please enter a number.")
        elif num == 0:
            print("bye <---------------------------")
            break
        elif num == 1:
            mean = sum(numbers)/len(numbers)
            print("The mean is: ", mean, "<---------------------------")
        elif num == 2:
            median = sorted(numbers) [len(numbers) // 2]
            print("The median is: ", median, "<---------------------------")
        elif num == 3:
            mode = max(numbers, key = numbers.count)
            print("The mode is: ", mode, "<---------------------------")
        else:
            numbers.append(num)
            print("Successfully added!")
            print(numbers)

def cal():
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