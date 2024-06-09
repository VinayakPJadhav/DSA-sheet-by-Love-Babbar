################################    Reverse An Array    ##############################



def reverse_array(arr):
    reverse_array=arr[::-1]


    print("Reverse Array is : ",end=" ")

    for i in reverse_array:
        print(i,end="  ")

arr = [11, 21, 51, 111, 121]
reverse_array(arr)
