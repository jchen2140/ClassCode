# just for my own reference, the hashtag makes this line a comment

# STEP 2

food_prices = {"chicken": 1.59, 
                "beef": 1.99, 
                "cheese": 1.00, 
                "milk": 2.00}

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