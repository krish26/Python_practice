n=input('Enter number of elements:' )
a=list(map(int,input('Enter the elements:').split()))
unique_ele=set(a)
unique_ele.sort()
print('The runner up score is:',unique_ele[-2])





