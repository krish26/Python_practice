my_array=[3,1,5,12,11,15]
n=len(my_array)
for i in range (n-1):
    swapped=False
    for j in range (n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j]
            swapped = True

    if not swapped:
        break


print("sorted array" , my_array)


