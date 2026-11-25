from budget_app import Category, create_spend_chart

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)

auto = Category('Auto')
auto.deposit(100, 'initial deposit')
auto.withdraw(20, 'gas')

print(food)
print(clothing)
print(food.get_balance())
print(food.check_funds(5000))
print(create_spend_chart([food, clothing, auto]))
