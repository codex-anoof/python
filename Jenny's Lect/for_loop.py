# Syntaax - for var_name in iterable:
#               statement(s)
# name = ['Anoof','Mazeen','Afshan']
# for i in name:
#      print(i,end = "\n")
#      if i == 'Anoof':
#           print("Anoof - Hey! It's me.")
#           continue
          
#EX 01 - print squares of numbers in list and create a list that contain squares of initial lisy
numbers = [2,4,8,9,10]
print(numbers)
print("Squares of above list are follows:")
squares = []
for i in numbers:
    square = i*i
    squares.append(square)
print(squares)

