'''Create three variables:
- city (a string): "Chemnitz"
- temp_celsius (a number): 28.5
- is_hot (a boolean): True if temp is above 25, False otherwise

Then compute:
- temp_fahrenheit using the formula: (celsius * 9/5) + 32
- temp_kelvin using: celsius + 273.15

Print each like this:
  Chemnitz: 28.5°C = 83.3°F = 301.65K
  Hot day? True'''

#create variables 
city = "Chemnitz"
temp_celsius = 28.5
is_hot = temp_celsius > 25

temp_fahrenheit = (temp_celsius * 9/5) + 32
temp_kelvin = temp_celsius + 273.15

print(f'{city}: {temp_celsius}°C = {temp_fahrenheit}°F = {temp_kelvin}K')
print(f'Hot day? {is_hot}')

