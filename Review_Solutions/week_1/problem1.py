def reverse_string(array):
    left , right = 0 , len(array) -1
    while left < right: 
        #this will take the first and last element and swap it and increment the left elem and decrement the right elem
        array[left] , array[right] = array[right] , array[left]
        left += 1
        right -= 1
    return array
    
try:
    user_input = list(map(str,input("Enter the array with spaces: ").split()))
    if len(user_input) < 2:
        print("Enter bigger array...")
        exit()
except ValueError:
    print("Enter Valid Input,,,, ")
   
print(reverse_string(user_input))
    

"""
array = list(map(int,input().split()))
reverse = arrray[::-1]
print(reverse)"""