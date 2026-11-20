class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, '*')
        lines = ''
        for item in self.ledger:
            desc = item['description'][:23]
            amt = f"{item['amount']:.2f}"[:7]
            lines += f"{desc:<23}{amt:>7}\n"
        return f"{title}\n{lines}Total: {self.get_balance():.2f}"


def create_spend_chart(categories):
    spent = []
    for cat in categories:
        total = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        spent.append(total)

    all_spent = sum(spent)
    percents = []
    for s in spent:
        pct = (s / all_spent * 100) if all_spent else 0
        percents.append(int(pct // 10) * 10)

    lines = ['Percentage spent by category']
    for i in range(100, -1, -10):
        row = f"{i:>3}| "
        for p in percents:
            row += 'o  ' if p >= i else '   '
        lines.append(row)

    lines.append('    ' + '-' * (3 * len(categories) + 1))

    names = [cat.name for cat in categories]
    longest = max(len(n) for n in names) if names else 0
    for i in range(longest):
        row = '     '
        for n in names:
            row += (n[i] if i < len(n) else ' ') + '  '
        lines.append(row)

    return '\n'.join(lines)
if __name__ == "__main__":
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
