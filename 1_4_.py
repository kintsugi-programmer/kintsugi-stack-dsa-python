def find_minimum(nums):
    '''
    Docstring for find_minimum
    
    :param nums: Find the minimum value in a list of numbers.
    '''
    if len(nums) == 0: # to handle cases containing nothing : []
        return None
    
    min_val = float('inf') # comparing wit biggest value, infinity
    
    for num in nums:
        if num < min_val:
            min_val = num
    
    return min_val