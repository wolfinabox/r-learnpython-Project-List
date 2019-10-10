# Goal

# Create three functions that allow the user to find the mean, median, and mode of a list of numbers. If you have access or know of functions that already complete these tasks, do not use them.

# Subgoals

#     In the mean function, give the user a way to select how many decimal places they want the answer to be rounded to. - DONE
#     If there is an even number of numbers in the list, return both numbers that could be considered the median. - DONE
#     If there are multiple modes, return all of them. - DONE

from math import floor,ceil
def mean(nums:list,decimal_places:int=2):
    return round(sum(nums)/len(nums),decimal_places)

def median(nums:list):
    return sorted(nums)[ceil(len(nums)/2.0)-1:floor(len(nums)/2.0)+1]

def mode(nums:list):
    modes=[]
    for num in nums:
        count=nums.count(num)
        if num in modes:continue
        if (not modes) or count>max(modes):
            modes.clear()
            modes.append(num)
        elif count==nums.count(modes[0]):
            modes.append(num)
    return modes

while True:
    numbers=[4,4,4,3,2,2,2,2,1,1]#list(map(float,input("Enter some numbers separated by spaces: ").split()))
    decimal_places=2#int(input("How many decimal places for mean?: "))
    print(f'Mean: {mean(numbers,decimal_places)}')
    print(f'Median: {median(numbers)}')
    print(f'Mode: {mode(numbers)}')
    break