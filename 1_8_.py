def find_longest_string(lst):
    longest_so_far= ""
    for s in lst:
        if len(s) > len(longest_so_far):
            longest_so_far = s
    return longest_so_far

list_of_words = ["Bali","Bhati", "Bhaskar"]

print(find_longest_string(list_of_words))
# Bhaskar