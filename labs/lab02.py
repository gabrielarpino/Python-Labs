def display_current_value():
  global current_value
  print('display_current_value', current_value)
  
def add(to_add):
  global current_value 
  global previous_value
  previous_value = current_value  
  current_value_add = current_value + to_add
  print(current_value_add)
  
def multiply(to_mult):
  global current_value
  global previous_value
  previous_value = current_value  
  current_value_mult = current_value*to_mult
  print(current_value_mult)
 
def divide(to_div):
  global current_value
  global previous_value
  previous_value = current_value
  current_value_div = current_value/to_div
  print(current_value_div)
  
def store():
  global current_value
  global memory
  memory = current_value
  
def recall():
  global memory
  print(memory)
  
def undo():
  global current_value
  global previous_value
  current_value = previous_value

def pow(n):
  global current_value
  global previous_value
  previous_value = current_value
  current_value_ex = current_value
  for i in range(n):
    current_value_ex *= current_value
  print(current_value_ex)
  
def pow(exponent):
  global current_value
  global previous_value
  previous_value = current_value
  result = 1
  for i in range(exponent):
    result = result * current_value
  
if __name__ == "__main__":
  print('Welcome to the calculator program.')
  global current_value
  current_value = 0
  print('Current Value:', current_value) 


