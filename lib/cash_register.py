#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_items = []


  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    for _ in range(quantity):
       self.items.append(title)
    self.previous_items.append({"title": title, "quantity": quantity, "price":price })

  def apply_discount(self):
      if self.discount > 0:
          self.total -= int(self.total * self.discount / 100)
          print(f'After the discount, the total comes to ${self.total}.')
      else:
          print("There is no discount to apply.")

  def void_last_transaction(self):
     if len(self.previous_items)>0:
        print(self.total)
        self.total -= (
          
            self.previous_items[-1]["price"]
            * self.previous_items[-1]["quantity"]
        )
        for _ in range(self.previous_items[-1]["quantity"]):
            self.items.pop()
        self.previous_items.pop()
        

aldi = CashRegister()
aldi.add_item('mcb',1000, 6)
aldi.add_item('mca',1000, 6)
aldi.void_last_transaction()