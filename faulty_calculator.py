'''Design a calculator which will correctly solve all problem except
45*5 = 555, 56+9 = 77 , 56/6 = 4 , 55-8 = 0

 your problem should take Operator
 :ADDITION, SUBSTRACTION, MULTIPLICATION, DIVIDE ,
 and return the result--------
'''

print("Select Operation: add,sub,mult,div ==")
op = input()
num1 = int(input("# Enter First no = "))
num2 = int(input("# Enter Secound no = "))


if op == 'mult' and (num1 == 45 and num2 == 5) or (num1 == 5 and num2 == 45):
    print("555")                #45*5 = 555

elif  op == 'add' and (num1 == 56 and num2 == 9) or (num1 == 9 and num2 == 56):
    print("77")                 #56+9 = 77

elif  op == 'div' and (num1 == 56 and num2 == 6) or (num1 == 6 and num2 == 56):
    print("4")                  #56/6 = 4

elif  op == 'sub' and (num1 == 55 and num2 == 8) or (num1 == 8 and num2 == 55):
    print("0")                  #55-8 = 0

elif op =='mult':
    m = num1 * num2
    print(m)

elif op =='add':
    p = num1 + num2
    print(p)

elif op =='div':
    d = num1 / num2
    print(d)

elif op =='sub':
    l = num1 + num2
    print(l)

else:
    print("Error! Check your input")
  
