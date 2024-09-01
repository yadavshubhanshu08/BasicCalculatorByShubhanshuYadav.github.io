print("First Calculator Made by Shubhanshu Yadav as his first PROJECT,")

print("Created with love by Shubhanshu, ")

print("ONLY FOR YOU")

print("Please Try This,")

print("Tell Your Query,")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Select Operation")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Percent")
print("6. Raised to Power")
print("7. Floor division")

choice = input("Enter choice(1/2/3/4/5/6/7): ")

if choice == '1':
  print(a + b)
elif choice == '2':
  print(a - b)

elif choice == '3':
  print(a * b)

elif choice == '4':
  print(a / b)

elif choice == '5':
  print(a % b)

elif choice == '6':
  print(a**b)

elif choice == '7':
  print(a // b)

if choice == '4':
  if b == 0:
    print("Cannot Divide by zero")

  else:
    print(a / b)

print("Thanks for Using This Basic Calculator")

print("Having Another query?.")

Y=(input("Yes"))
N=(input("NO"))

print("Select")

print('Yes')
print('N')

choice=input("Enter Choice(Y/N): ")