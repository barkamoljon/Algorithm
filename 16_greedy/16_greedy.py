def greedy_algorithm(items, capacity):
  # Sort the items by their profit per weight ratio
  items.sort(key=lambda item: item.profit / item.weight, reverse=True)
  
  # Create a knapsack to store the items
  knapsack = []
  # Iterate over the items
  for item in items:
    # If the item fits in the knapsack, add it
    if item.weight <= capacity:
        knapdack.append(item)
        capacity -= item.weight
        
  return knapsack
