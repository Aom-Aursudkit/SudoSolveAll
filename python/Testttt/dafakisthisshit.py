# def ps(n):
#     strn = str
#     fac = 1
#     for i in range(1, n + 1):
#         fac *= i
#     print(fac)
    
#     count = []
#     for i in range(1,n+1):
#         count.append(i)
#     print(count)
#     for i in range(fac):
#         temp = count
#         for ii in range(n):
#             ans

# print(ps(3))

def generate_permutations(n):
    # Initialize an empty list to store permutations
    permutations_list = []
    
    # Create an initial permutation as a list of integers from 1 to n
    current_permutation = list(range(1, n + 1))
    
    # Use a flag to determine when to stop
    done = False
    
    while not done:
        # Append the current permutation to the list
        permutations_list.append(''.join(map(str, current_permutation)))
        
        # Find the rightmost element smaller than its neighbor
        i = n - 2
        while i >= 0 and current_permutation[i] >= current_permutation[i + 1]:
            i -= 1
        
        # If there is no such element, we are done
        if i == -1:
            done = True
        else:
            # Find the smallest element to the right of i and greater than current_permutation[i]
            j = n - 1
            while current_permutation[j] <= current_permutation[i]:
                j -= 1
            
            # Swap the elements at positions i and j
            current_permutation[i], current_permutation[j] = current_permutation[j], current_permutation[i]
            
            # Reverse the elements to the right of i
            current_permutation[i + 1:] = reversed(current_permutation[i + 1:])
    
    return permutations_list

# Example usage for n = 3
permutations_list = generate_permutations(3)

# Print the result in list format
print(permutations_list)

