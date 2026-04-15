#1. Countdown 
def countdown(num):
    list = [];
    for i in range(num , -1 , -1):
        list.append(i)
    return list;
print(countdown(5))


#2. Print and Return
def print_and_return(list):
    print(list[0])
    return(list[1])
second_item = print_and_return([1,2]) 
print(second_item)


#3. First Plus Length
def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length([1,2,3,4,5]))
#4. Values Greater than Second
def values_greater_than_second(list):
    list_length = len(list)
    if(list_length < 2):
        return False
    new_list = []
    counter = 0
    for i in range(list_length):
        if(list[i] > list[1]):
            new_list.append(list[i])
            counter = counter+1
    print(counter)
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))
            
#5. This Length, That Value
def length_and_value(size , value):
    list = []
    for i in range(size):
        list.append(value)
    return list

print(length_and_value(6,2))