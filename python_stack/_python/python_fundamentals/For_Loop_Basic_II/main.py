#1. Biggie Size
def biggie_size(lst):
    for i in range(len(lst)):
        if(lst[i] > 0):
            lst[i] = "big"
    return lst

print(biggie_size([-1, 3, 5, -5]))

#2. Count Positives
def count_positives(lst):
    positives_counter = 0
    for num in lst:
        if num > 0:
            positives_counter += 1
    lst[len(lst) - 1] = positives_counter
    return lst

print(count_positives([-1,1,1,1]) )

#3. Sum Total
def sum_total(lst):
    sum = 0
    for num in lst:
        sum += num
    return sum
print(sum_total([1,2,3,4]))

#4. Average
def average(lst):
    if len(lst) == 0:
        return 0
    nums_total = sum_total(lst)
    nums_count = len(lst)
    return nums_total / nums_count

print(average([1,2,3,4]) )

#5. Length
def length(lst):
    count = 0
    for item in lst:
        count += 1
    return count

#6. Minimum 
def minimum(lst):
    min_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_val:
            min_val = lst[i]

    return min_val

#7. Maximum 
def maximum(lst):
    max_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]

    return max_val

#8. Ultimate Analysis
def ultimate_analysis(lst):
    total = sum_total(lst)
    min = minimum(lst)
    max = maximum(lst)
    avg = average(lst)
    
    result = {
        'sumTotal': total,
        'average': avg,
        'minimum': min,
        'maximum': max,
        'length': len(lst)
    }
    return result

print(ultimate_analysis([37,2,1,-9]))

#9. Reverse lst 
def reverse_lst(lst):
    pointer = 1
    for i in range(len(lst) // 2):
        lst[i] , lst[len(lst) - pointer] = lst[len(lst) - pointer] , lst[i]
        pointer += 1
    return lst
    
print(reverse_lst([37,2,1,-9]))



    
    