
def two_sum(nums: list[int], target: int) -> list[int]:
    values = {}

    for index, value in enumerate(nums):
        remaining = target - value

        if remaining in values:
            return [values[remaining], index]

        else:
            values[value] = index


list_item = [7, 11, 9, 2]
target = 9

print(two_sum(list_item, target))


# This algorithm can only be used if and only if the list is sorted
# Time complexity for this is O(n)
# Also in two sum problems looking for indices, it's bad idea to sort an array
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    first = 0
    last = len(nums) - 1

    while first < last:
        if (nums[first] + nums[last] == target):
            return [first, last]

        elif (nums[first] + nums[last]) > target:
            last -= 1

        else:
            first += 1


list_item = [2, 7, 11, 15]
target = 9

print(two_sum_sorted(list_item, target))


# This algorithm can be used on both sorted and unsorted list
# But it is worst with time complexity of O(n^2)
def two_sum_worst_time(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


list_item = [2, 11, 7, 15]
target = 9

print(two_sum_worst_time(list_item, target))
