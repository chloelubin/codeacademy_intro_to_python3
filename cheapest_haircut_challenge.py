# Help hairdresser advertise cheapest haircuts

# list of all hairstyles offered at hairdresser
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# list of prices associated with hairstyles listed above
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# number of haircuts completed the previous week by hairstyle
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# set price to 0
total_price = 0

# reiterate through all prices to print the sum
for price in prices:
    total_price += price
    print(total_price)

# determine average price of a haircut
average_price = total_price / len(prices)

print("Average Haircut Price: " + str(average_price))

# reduce the price of all haircuts by $5
new_prices = [price - 5 for price in prices]

print(new_prices)

# set total_revenue to 0
total_revenue = 0

# reiterate through new_prices to determine revenue generated the previous week
for i in range(0, len(hairstyles)):
    tot_rev = prices[i] * last_week[i]
    total_revenue += tot_rev
    print("Total Revenue: " + str(total_revenue))

# determine average daily revenue based on total_revenue
average_daily_revenue = total_revenue / 7

# determine all haircuts under $30 based on list enumeration created for new_prices
cuts_under_30 = [hairstyles[i] for i in range(0, len(new_prices - 1)) if new_prices[i] < 30]

# print all haircuts under $30
print(cuts_under_30)
