# # a=int(input("Enter a number of elements you want to put in list1"))
# # list1
# # for i in range (a):
# #     print("Enter the " ,i+1, "elemnet-" )
# #     b=int(input())
# #     list1[i]=b
# # a2=int(input("Enter a no. of elements you want to put in list2"))    
# # list2[a2]=0
# # for j in range (a2):
# #     print("Enter the " ,j+1, "elemnet-")
# #     b2=int(input())
# #     list2[j]=b2
# # common=[]
# # for element in list1:
# #     if(element in list2):
# #         common.append(element)
# # print(common)
# list=[]
# n=int(input("Enter a number of elements you want tom add"))
# for i in range(0,n):
#     print(" enter the",i+1,"element:")
#     d=int(input())
#     list.append(d)
# print(list)
# lst=["Python Programming ","DBMS","Web Tech","Engg"]
# lst2=[]
# lst.append(12)
# lst.append(122)
# lst.append(2)
# lst.extend("123")
# lst.extend([32,"abc"])
# lst=[23,"bill",67,89]
# lst.remove("bill")
# # print(lst)
# print(len(lst))
# tup=(3,4,5,6)
# tup=tup+(44,)
# print(tup)
tup=((1,2),(3,4),(5,6))
top=()
for i in range(0,3):
    for j in range(0,2):
        top=top+(tup[i][j],)
print(top)
