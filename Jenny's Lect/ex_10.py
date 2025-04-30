#Love Calculator
name_1 = input("Enter your name : ")
name_2 = input("Enter your partner's name : ")
combine_name = name_1 + name_2
lower_case_name = combine_name.lower()
t = lower_case_name.count("t")
r = lower_case_name.count("r")
u = lower_case_name.count("u")
e = lower_case_name.count("e")
true = t + r + u + e
l = lower_case_name.count("l")
o = lower_case_name.count("o")
v = lower_case_name.count("v")
e = lower_case_name.count("e")
love =  l + o + v + e
love_score = int(str(true) + str(love))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score} and you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score} and you are alright together.")
else:
    print(f"Your Score is {love_score}")
