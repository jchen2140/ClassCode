# just for my own reference, the hashtag makes this line a comment

# STEP 2

food_prices = {"chicken": 1.59, 
                "beef": 1.99, 
                "cheese": 1.00, 
                "milk": 2.00}

def total_price(Dict, item1, item2):
    sum = Dict[item1] + Dict[item2]
    print(" The total price of " + item1 + " and " + item2 + " is $", str(sum))
total_price(food_prices, "beef", "cheese")


# OR

def total_price(item1, item2):
    price1 = food_prices[item1]
    price2 = food_prices[item2]
    return price1 + price2

print("Price of cheese and beef: $" + str(total_price("beef", "cheese")))
print(type(total_price("milk", "cheese")))
#type let's you know what type it is ex: float, str, int, etc
#to make both the same type, wrap one of the values around something like str as shown above

# STEP 3 from lab 4 
def price_difference(item1, item2):
    price1 = food_prices[item1]
    price2 = food_prices[item2]
    difference = price1 - price2

    if price2 > price1:
        difference = price2 - price1
    else:
        difference = price1 - price2


    return difference
print("The difference between beef and cheese: $" + str(price_difference("cheese", "beef")))

# STEP 3
nctdream_age = {"Mark Lee": 21,
            "Park Jisung": 19,
            "Na Jaemin": 20,
            "Lee Haechan": 21}

# STEP 4
chicken_price = food_prices["chicken"]
print(chicken_price)
beef_price = food_prices["beef"]
print(beef_price)
cheese_price = food_prices["cheese"]
print(cheese_price)
milk_price = food_prices["milk"]
print(milk_price)

# STEP 5
mark_age = nctdream_age["Mark Lee"]
print(mark_age)
jisung_age = nctdream_age["Park Jisung"]
print(jisung_age)
jaemin_age = nctdream_age["Na Jaemin"]
print(jaemin_age)
haechan_age = nctdream_age["Lee Haechan"]
print(haechan_age)

# STEP 5 cont
nctdream_age['Mark Lee'] = 22
print(nctdream_age)

# how to add something to your dictionary
nctdream_age['Zhong Chenle'] = 19
print(nctdream_age)

# to delete
del nctdream_age['Zhong Chenle']
print(nctdream_age)