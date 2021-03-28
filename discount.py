print('How much is the item?')
itemPrice = float(input())
print('What is the discount percentage')
discountPercent = int(input())
if discountPercent > 9:
    discountPercent /= 100
elif discountPercent < 10:
    discountPercent /= 10
discount = itemPrice * discountPercent
finalPrice = itemPrice - discount
print('The item will cost you',round(finalPrice, 2))

print('What is your total bill?')
totalBill = float(input())
print('What precent will you tip?')
tipPercent = int(input())
if tipPercent > 9:
    tipPercent /= 100
elif tipPercent < 10:
    tipPercent /= 10
final = totalBill * tipPercent

print('You will tip $',round(final, 2))     