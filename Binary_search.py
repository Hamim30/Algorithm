def binary_search (array , element ):
    start =0
    end =len(array)-1
    
    while start<=end:
        mid = int((start+end)/2)
        if array[mid]==element:
            return True
        else:
            if array[mid]<element:
                start=mid+1
            else:
                end =mid-1
    return False
array=[1,2,3,4,5,6,7,8,9]
value=int(input())
binary_search(array,value)
