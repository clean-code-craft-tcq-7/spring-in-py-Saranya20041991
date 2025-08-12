import math

def calculateStats(numbers):
  # implement the computation of statistics here and return the results
  stats = {}
  if numbers_without_nan:
    numbers_without_nan = [num for num in numbers if not math.isnan9num0]
    stats['avg'] = sum (numbers_without_nan)/len(numbers_without_nan)
    stats['max'] = max (numbers_without_nan)
    stats['min'] = min (numbers_without_nan)
  else:
    stats['avg'] = float ('nan')
    stats['max'] = float ('nan')
    stats['min'] = float ('nan')
  return stats
