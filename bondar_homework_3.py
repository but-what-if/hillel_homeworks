value = int(input('Enter the number: '))
new_value = value / 2 if value < 100 else -value
print(new_value)

####################################################

value = int(input('Enter the number: '))
new_value = 1 if value < 100 else 0
print(new_value)

####################################################

value = int(input('Enter the number: '))
new_value = True if value < 100 else False
print(new_value)

####################################################

my_str = 'QwEr'
my_str = my_str.upper()
print(my_str)

####################################################

my_str = 'QwEr'
my_str = my_str.lower()
print(my_str)

####################################################

my_str = 'QwEr'
if len(my_str) < 5:
  my_str = my_str + my_str
else:
  pass
print(my_str)

####################################################

my_str = 'QwEr'
if len(my_str) < 5:
  my_str = my_str + my_str[::-1]
else:
  pass
print(my_str)

####################################################

my_str = 'Hello, world! 25th of September'
for symbol in my_str:
  if symbol.isdigit() or symbol.isalpha():
    print(symbol)

####################################################

my_str = 'Hello, world! 25th of September'
for symbol in my_str:
  if not (symbol.isdigit() or symbol.isalpha()):
    print(symbol)

###################################################

my_str = 'Hello, world! 25th of September'
for symbol in my_str:
  if not (symbol.isdigit() or symbol.isalpha() or symbol.isspace()):
    print(symbol)







