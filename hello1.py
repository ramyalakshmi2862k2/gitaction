print("hello Ramya!")
import random

def roll_dice():
  """Simulates the roll of a six-sided die and returns the result."""
  return random.randint(1, 6)

# Example usage:
result = roll_dice()
print(f"You rolled a: {result}")