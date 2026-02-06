def sum_numbers(nums):
    if len(nums) == 0:
        return 0

    s = 0
    for n in nums:
        s+=n
    return s

l1 = [1,23,45,566]
print(sum_numbers(l1))
# 635