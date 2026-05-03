#List of fruits
fruits=["apple", "banana", "apple", "orange", "banana", "apple","orange","Grapes","banana"]

# Create empty dictionary
fruit_freq = {}

# Traverse each word
for fruit  in fruits:
    
    # Check if word already exists
    if fruit in fruit_freq:
        fruit_freq[fruit] += 1   # Increase count
    else:
        fruit_freq[fruit] = 1    # Initialize count

# Print frequency dictionary
print("Frequency:", fruit_freq)

