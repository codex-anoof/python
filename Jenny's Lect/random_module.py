import random

random_1 = random.randint(1, 10)
random_2 = random.randrange(1, 10)
random_3 = [20,30,50,-90,1000,34,56,47,89,76,54,34,23,12,11,10]
random_4 = random.choice(random_3)
random_5 = random.sample(random_3, 5)
random_6 = random.uniform(1, 10)
random_7 = random.random()
print(random_1, random_2, random_3, random_4, random_5, random_6, random_7)
print("random_1:", random_1)
print("random_2:", random_2)
print("random_3:", random_3)
print("random_4:", random_4)
print("random_5:", random_5)
print("random_6:", random_6)
print("random_7:", random_7)