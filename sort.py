
def insertion(list):
  for i in range(len(list)):
    for j in range(len(list)):
       if list[j]<=list[i]:
          temp=list[i]
          list[i]=list[j]
          list[j]=temp
  print (list)


def selection(list):
  for i in range(len(list)):
    for j in range(i):
       if list[j]<=list[j+1]:
          temp=list[j]
          list[j]=list[j+1]
          list[j+1]=temp
  print (list)
def bubble(list):
  for i in range(len(list)):
    for j in range(len(list)-1):
      if list[j]<=list[j+1]:
         temp=list[j]
         list[j]=list[j+1]
         list[j+1]=temp
  print(list)

list=[3,8,2,15,1,4,10,5,9,7,6]
temp=0
bubble(list)
temp=0
list=[3,8,2,15,1,4,10,5,9,7,6]
insertion(list)
temp=0
list=[3,8,2,15,1,4,10,5,9,7,6]
selection(list)

