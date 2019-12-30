#determine ground shipping cost
def ground_ship(weight):
  if weight <= 2:
    return weight * 1.5 + 20.00
  elif weight > 2 and weight <= 6:
    return weight * 3.00 + 20.00
  elif weight > 6 and weight <= 10:
    return weight * 4 + 20.00
  else:
    return weight * 4.75 + 20.00

#test ground shipping cost function  
print(ground_ship(100))

#create a variable with a flat rate value
premium_ground = 125.00

#determine shipping cost by drone
def drone_ship(weight):
  if weight <= 2:
    return weight * 4.5 + 0
  elif weight > 2 and weight <= 6:
    return weight * 9.00 + 0
  elif weight > 6 and weight <= 10:
    return weight * 12 + 0
  else:
    return weight * 14.25 + 0
  
#test drone shipping cost function
print(drone_ship(1.5))

#determine cheapest shipping method between: ground shipping, premium ground shipping, and drone shipping methods.
def cheapest_shipping(weight):
  is_ground_cheapest = ground_ship(weight) < premium_ground and ground_ship(weight) < drone_ship(weight)
  
  is_premium_cheapest = premium_ground < ground_ship(weight) and premium_ground < drone_ship(weight)
        
  is_drone_cheapest = drone_ship(weight) < ground_ship(weight) and drone_ship(weight) < premium_ground
  
  if is_ground_cheapest:
    print("You should ship using ground shipping, it will cost "+str(ground_ship(weight)))
  
  elif is_premium_cheapest:
    print("You should ship using premium ground shipping, it will cost "+str(premium_ground))

  else:
    print("You should ship using drone shipping, it will cost "+str(drone_ship(weight)))

#test cheapest_shipping function
print(cheapest_shipping(10))
