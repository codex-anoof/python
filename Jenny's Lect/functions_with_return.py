#Functions with Return value
''' print("method 1 : functions with return")
def add(num_1,num_2):
    sum = num_1 + num_2
    print(sum)
sum = add(50,43)
print(sum)
print("------------------------------")

# Above Function with print is not have value when we use it as variable

print("method 2 : Function with return keyword")
def add(num_1,num_2):
    sum = num_1 + num_2
    return sum
num1 = int(input("Enter your first number to add : "))
num2 = int(input("Enter your second number to calculate the sum : "))
sum = add(num1,num2)
print(sum)
'''
print("-----------------------------------------------------------")
print("Jenny's Quiz")
print("------------")
def name_title(name,name_last):
    name = name + " " + name_last
    name = name.title() 
    return name
print(name_title("jenny","KHATRI"))
