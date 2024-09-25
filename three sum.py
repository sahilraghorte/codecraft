def three_sum(nums):
    # Sort the array to make it easier to avoid duplicates and use two pointers
    nums.sort()
    triplets = []
    
    # Loop through each element as the fixed element
    for i in range(len(nums) - 2):
        # Skip the duplicates for the fixed element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Use two pointers to find the remaining two numbers
        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                # If the triplet is found, add it to the result
                triplets.append([nums[i], nums[left], nums[right]])
                
                # Move both pointers to the next distinct element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < 0:
                # Move the left pointer to the right to increase the sum
                left += 1
            else:
                # Move the right pointer to the left to decrease the sum
                right -= 1
    
    return triplets

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print("Unique triplets that sum to zero:", result)
