#39有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

def insert_sort_array(array, num):
    low =0
    high = len(array) -1

    while (high - low) > 1:
        mid = low + int((high - low) /2)
        if array[mid] > num:
            high = mid
        else:
            low = mid
    array.insert(low+1, num)

aa = [1, 3, 4, 6, 7, 10, 19]

insert_sort_array(aa, 5)
print(aa)