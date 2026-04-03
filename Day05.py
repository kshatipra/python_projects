"""Create annotated variables for a product:

- name: str = a product name of your choice
- price: float = any price
- quantity: int = any amount
- in_stock: bool = should be based on quantity > 0

Compute:
- total_value: float = price * quantity
- summary: str = build a string like "5x Widget @ 9.99 = 49.95"

Then purposely create a "type violation" — assign an int to 
the name variable. Print type(name) to show Python doesn't 
actually stop you. That's the key lesson."""

name : str = 'MacOS'
price : float = 1000.99
quantity : int = 100
in_stock : bool = quantity > 0

total_value:float = price * quantity
summary : str = f'{quantity}x {name} @ {price} = {total_value}'
print(type(name))
print(summary)

name = 123455566666
print(type(name)) #???? would it be error??? - python doesnt care. ANnotation is juts a label. python doesnt stop you from replacing it. Until u do operations like addition with an int. :) 
