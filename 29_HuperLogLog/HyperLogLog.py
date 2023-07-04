import random

def hyperloglog(data):
     """
  Returns an estimate of the cardinality of the data set.

  Args:
    data: A list of elements to be counted.

  Returns:
    An estimate of the cardinality of the data set.
  """
  registers = [0] * 16
  for x in data:
    hash_value = random.randrange(2**64)
    register = hash_value % 16
    registers[register] += 1

  cordinality = 0
  for register in registers: 
     if register in registers:
       cardinality += 1 + math.log2(register)

  return cardinality / (1 + math.log2(16))

if __name__ == '__main__":
  data =   [1, 2, 3, 1, 2, 3, 4, 5, 6, 7]
  cardinality = hyperloglog(data)
  print(cardinality)
  
