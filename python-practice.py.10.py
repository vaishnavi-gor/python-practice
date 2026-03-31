my_list = [4, 2, 9]

smallest = my_list[0]
num= 1

while num < len(my_list):
    if my_list[num] < smallest:
        smallest= my_list [num]
        
    num = num + 1
    
print(smallest)

my_list = [4, 2, 9]

biggest = my_list[0]
num = 1

while num < len(my_list):
    if my_list[num] > biggest:
        biggest = my_list[num]
        
    num = num + 1

print(biggest)    