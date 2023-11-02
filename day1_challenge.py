#sales profit

buying = float(input("Enter initial cost: "))
selling = float(input("Enter selling price: "))
units = float(input("Enter no of units sold: "))

# print((selling_price - cost_of_item)* no_of_units)

def profit_computation(buying, selling, units): # function declaration
    #function definition
    profit = (selling-buying)*units
    return profit
print(profit_computation(buying, selling, units)) # function call