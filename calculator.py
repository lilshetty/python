a=input("enter the value of the first number :")
a=int(a)
b=input("enter the value of the second number :")
b=int(b)
o=input("enter the operation to be performed :")
#print("1.add 2.sub 3.multiply 4.divide 5.exit")
if o=="+":
  print(a+b)
else:
  if o=="-":
    print(a-b)
  else:
    if o=="*":
      print(a*b)
    if o=="/":
      if b==0:
        print("divide by zero error")
      else:
        print(a/b)
