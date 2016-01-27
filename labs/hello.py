def display_current_value():
  global current_value
  print('display_current_value', current_value)
  
def add(to_add):
  global current_value 
  current_value_add = current_value + to_add
  global add_step
  add_step = current_value_add
  print(current_value_add)
  
def multiply(to_mult):
  global current_value
  current_value_mult = current_value*to_mult
  global mult_step
  mult_step = current_value_mult
  print(current_value_mult)
 
def divide(to_div):
  global current_value
  current_value_div = current_value/to_div
  global div_step
  div_step = current_value_div
  print(current_value_div)
  
def store():
  global current_value
  global memory
  memory = current_value
  
def undo():
  global current_value
  global add_step
  global mult_step
  global div_step
  
  

  
if __name__ == "__main__":
  print('Welcome to the calculator program.')
  global current_value
  current_value = 0
  print('Current Value:', current_value) 