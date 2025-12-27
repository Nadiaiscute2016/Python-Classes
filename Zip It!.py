s1 = {2, 3, 1}
s2 = ('b', 'a', 'c')
s3 = list(zip(s1, s2))
print(s3, "/n")
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90 ]
for x, y in zip(list1, list2[::-1]):
    print (x, y)
stocks = ['reliance', 'infosys', 'tcs']
prices = [9000, 5000, 4003]
new_dict = {stocks: prices for stocks ,prices in zip(stocks,prices)}
print('/n{}'.format(new_dict))