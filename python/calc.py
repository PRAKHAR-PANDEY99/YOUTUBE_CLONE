print("Mathe")
a=int(input(" Enter a 1 number--"))
b=int(input(" Enter a  2 number--"))
d=input("Enter what type of operation you want to do- ex-*,-,/,+")
if(d=="*"):
    print(a*b)
elif(d=="-"):
    print(a,"-",b"=",a-b)
elif(d=="/"):
    print(a,"/",b,"=",a/b)
elif(d=="+"):
    print(a,"+",b,"=",a+b)
else:
    print("You entered non existing operation or null")
print("Now we are adding your words to make sentences")
q=int(input("Enter how many words you want to give"))
w=" "
for i in range(1,q+1):
    print(" enter a ",i," Word \t")
    e=input()
    w=w+" "+e
print("Sentence formed-",w)
num=float(input(" enter   a   nmber"))


a=int(input(" Enter a 1 number--"))
if(a>0):
    print("Positive")
    if(a%2==0):
        print("Even")
    else:
        print("odd")
elif(a<0):
    print("Negative")
    if(a%2==0):
        print("Even")
    else:
        print("odd")
elif(a==0):
    print("NUMBER IS 0")
elif(type(a)==type(4.5)):
    print(" Float number(decimal)")
else:
    print("You entered something else ")
