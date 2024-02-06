def add(x, y):
  return x + y

def divide(numerator, demoninator):
  if demoninator == 0:
    raise ValueError('Cannot divide by zero!')
  return numerator/demoninator