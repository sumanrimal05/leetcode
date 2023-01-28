# Time complexity O(n)
def maxArea(height: list[int]) -> int:
    high = 0
    left = 0

    right = len(height)-1
    while left < right:
        minimum_value = min(height[left], height[right])
        container_capacity = minimum_value * (right-left)
        if container_capacity > high:
            high = container_capacity
        if (height[left] < height[right]):
            left += 1
        else:
            right -= 1
    return high


height = [1, 7, 6, 2, 5, 4, 8, 3, 8]

print(maxArea(height))
