
#Write a program to sort list of strings (similar to that of dictionary)
def sort_strings(strings):
    return sorted(strings)

strings = ["banana", "apple", "cherry", "date", "fig"]
sorted_strings = sort_strings(strings)
print(sorted_strings)
strings = ["orange", "banana", "apple", "watermelon", "cherry", "grape", "date", "fig", "kiwi"]
sorted_strings = sort_strings(strings)
print(sorted_strings)
