import time

name = input("enter your name ")
time = int(time.strftime("%H"))
# print(time)
if (time > 0 and time < 12):
  print("good morning", name, "lets play KBC")
elif (time > 12 and time < 16):
  print("good afternoon", name, "lets play KBC")
else:
  print("good evening", name, "lets play KBC")
# ok=input("type 1 to continue and 0 to exit ")
ques = [
  "what is nationalbird",
  "who is the author of the book power of subconsious mind",
  "who is the author of the book how to win friends and influence people",
  "who is saket gokhale", "who is harry"
]
ans1 = ["crow", "peocock", "owl", "sparrow"]
ans2 = ["joseph murphy", "david goggins", "james clear", "dale carnegie"]
ans3 = ans2.copy()
# print(ans3)
ans4 = ["fitness influencer", "actor", "coder", "drug dealer"]
ans5 = ans4.copy()
m = [1000, 2000, 3000, 4000, 5000]
print(ques[0])
for i in ans1:
  print(i)
q1 = input("enter the option in lower case \n")
if q1 == ans1[1]:
  print("correct answer! and next question is\n")
else:
  print("wrong answer! next question\n\n")
print(ques[1])
for i in ans2:
  print(i)
q2 = input("enter the option in lower case\n")
if q2 == ans2[0]:
  print("correct answer! and next question is\n")
else:
  print("wrong answer! next question\n")
print(ques[2])
for i in ans3:
  print(i)
q3 = input("enter the option in lower case\n")
if q3 == ans3[3]:
  print("correct answer!next question is\n")
else:
  print("wrong answer! next question\n")
print(ques[3])
for i in ans4:
  print(i)
q4 = input("enter the option in lower case")
if q4 == ans4[0]:
  print("correct answer! and next question is\n")
else:
  print("wrong answer! next question\n")
print(ques[4])
for i in ans5:
  print(i)
q5 = input("enter the option in lower case")
if q5 == ans5[2]:
  print("correct answer! thanks for playing\n")
else:
  print("wrong answer! thanks for playing\n")
