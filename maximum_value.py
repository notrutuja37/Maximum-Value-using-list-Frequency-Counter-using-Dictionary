# Function to find maximum value in a list
def find_max_value(numbers):
    
    # Check if list is empty
    if len(numbers) == 0:
        return None   # Return None if empty
    
    # Assume first element is maximum
    max_value = numbers[0]

    # Traverse list
    for num in numbers:
        # Compare each element with current max
        if num > max_value:
            max_value = num   # Update max value

    return max_value   # Return final maximum


# Sample input list
data = [10, 26, 89, 40, 100]

# Function call
result = find_max_value(data)

# Print result
print("Maximum value:", result)
