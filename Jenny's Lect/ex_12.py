 #I create this for payt heb bill within friends randomly
import random
names = input("Etner the names of your friends separated by a comma: ")
names = names.split(",")
length = len(names)
random_number = random.randint(0, length - 1)
print("The person who will pay the bill is:", names[random_number])
# I create this for payt heb bill within friends randomly