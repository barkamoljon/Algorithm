def binary_search(list, item):
  # Initialize low and high pointers
  low = 0
  high = len(list) - 1

  # Iterate while low <= high
  while low <= high:
    # Calculate the middle index
    mid = (high + low) // 2

    # Get the element at the middle index
    guess = list[mid]

    # If the guess is equal to the item, return the index
    if guess == item:
      return mid

    # If the guess is greater than the item, set the high pointer to the middle index - 1
    elif guess > item:
      high = mid - 1

    # Otherwise, set the low pointer to the middle index + 1
    else:
      low = mid + 1

  # If the item is not found, return None
  return None
      
