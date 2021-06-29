def triangleArea(base,height):
    area = base*height/2
    return area

area = triangleArea(2,4)
print(triangleArea(2,4))

# How to create a function
def squareArea(side):
    area = side*side
    return area
print(squareArea(4))

def rect_area(length, width):
    area = length*width
    return area
print("The area of a 4 x 6 rectangle is:")
print(rect_area(4,6))


# 2nd half of lab 4
# STEP 2
Menu = {"Fries": 2.00, "Soda": 1.99, "Hamburger": 5.00, "Burrito": 4.50}

def foodSum(Dict, item1, item2):
    sum = Dict[item1] + Dict[item2]
    print("The total price of " + item1 + " and " + item2 + " is $" + str(sum))
    sum *= 1.0925
    print("With tax that will be $" + str(round(sum,2)))
    
foodSum(Menu, "Fries", "Soda")


def foodSum2(Dict, *args):
    sum = 0
    text = "The total price of your order of"
    for keys in args:
        if keys in Dict:
            sum += Dict[keys]
            text += keys + " "
    text += "is $" + str(sum)
    print(text)

foodSum2(Menu, "Hamburger", "Soda", "Fries")

# Step 3
price_difference = {"Fries": 2.00, "Hamburger": 5.00} 

def foodDifference(Dict, item1, item2):
    foodDifference = Dict[item2] - Dict[item1]
    print("The difference between" + item1 + " and " + item2 + " is $" + str(foodDifference))
foodDifference(price_difference, "Fries", "Hamburger")

#OR

def price_difference(item1, item2):
    price1 = Menu[item1]
    price2 = Menu[item2]
    difference = price1 - price2
    if price1 > price2:
        difference = price1 - price2
    else:
        difference = price2 - price1
    difference = price1 - price2
    return difference
    
print("The difference between Hamburger and Fries: $" + str(price_difference("Fries", "Hamburger")))

# Step 4

restock = {"Yeezy": 8, "Air Force": 5}

def shoe_number(shoe1, num):
    shoe_number = restock[shoe1] *num
    print(shoe_number)
shoe_number("Yeezy", 3)

shoes = {'Jordan 13': 1, 'Yeezy': 8, 'Foamposite': 10, 'Air Max': 5, 'SB Dunk': 20 }
def restock(shoe_type, count):
    shoe_type = shoes[shoe_type] * count
    return shoes[shoe_type]
    # 8 = 8*3
    # 24
    #shoes[Yeezy] =

restock("Yeezy", 3)
print(restock("Yeezy", 3))
# Step 5
clearance_sale = {"SB Dunk": 20, "Air Force": 40}

def product_price(item1, num):
    product_price = clearance_sale[item1] /num
    print(product_price)
product_price("SB Dunk", 5)

# Step 6
number_of_shoes = {"SB Dunk": 20, "Air Force": 40}

def shoe_ratio(shoe1, shoe2):
    shoe_ratio = number_of_shoes[shoe1]//number_of_shoes[shoe2]
    print(shoe_ratio)
shoe_ratio("Air Force", "SB Dunk")




    
