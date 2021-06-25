# step & 2
list_of_cities = ['dallas', 'oakland', 'new york city', 'seattle', 'los angeles', 'miami', 'denver', 'new orleans', 'boston']

print(list_of_cities[0:3]) # 0,1,2

# step 3
list_of_nct_members = ['taeil', 'johnny', 'taeyong', 'kun', 'ten', 'yuta', 'doyoung', 'jaehyun', 'winwin', 'jungwoo']
three_members = list_of_nct_members[6:9]

# step 4
print(three_members)

# step 5
list_of_cities[1] = 'San Francisco'
list_of_cities[2] = 'Brooklyn'
list_of_cities[4] = 'Hollywood'
list_of_cities[5] = 'Tampa'

# step 6
list_of_cities.append('oakland')
list_of_cities.extend(['new york city', 'los angeles'])
list_of_cities.insert(1, 'Miami')

# step 7
del list_of_cities[3]
list_of_cities.pop(0)
list_of_cities.remove('denver')
print(list_of_cities)