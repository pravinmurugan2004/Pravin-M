my_list = [1,2,3,4,5,5,4]
unique_list=[]
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
     
          