import random

class BlommFilter:
    def __init__(self, size, hash_functions):
        self.size = size
        self.hash_functions = hash_functions
        self.bits = [False] * size

    def add(self, element):
        for hash_function in self.hash_functions:
            index = hash_functions(element) % self.size
            self.bits[index] = True

    def contains(self, element):
        for hash_function in self.hash_functions:
            index = hash_function(element) % self.size
            if not self.bits[index]:
                return False
        return True

  # Create a Bloom filter with a size of 100 bits and 3 hash functions.
bloom_filter = BloomFilter(100, 3)

# Add some elements to the Bloom filter.
bloom_filter.add("hello")
bloom_filter.add("world")

# Check if some elements are in the Bloom filter.
print(bloom_filter.contains("hello"))  # True
print(bloom_filter.contains("world"))  # True
print(bloom_filter.contains("goodbye"))  # False
