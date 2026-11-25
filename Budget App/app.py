from flask import Flask, request
from budget_app import Category, create_spend_chart

app = Flask(__name__)
cats = {n: Category(n) for n in ['Food', 'Clothing', 'Auto']}


@app.route('/', methods=['GET', 'POST'])
def home():
    msg = ''
    if request.method == 'POST':
        cat = cats[request.form['category']]
        amount = float(request.form['amount'])
        desc = request.form['description']
        if request.form['action'] == 'deposit':
            cat.deposit(amount, desc)
        elif not cat.withdraw(amount, desc):
            msg = 'Insufficient funds'

    options = ''.join(f'<option>{n}</option>' for n in cats)
    ledgers = '\n\n'.join(str(c) for c in cats.values())
    chart = create_spend_chart(list(cats.values()))

    return (
        '<h1>Budget App</h1>'
        '<form method="post">'
        f'<select name="category">{options}</select> '
        '<input name="amount" type="number" step="0.01" placeholder="Amount" required> '
        '<input name="description" placeholder="Description"> '
        '<button name="action" value="deposit">Deposit</button> '
        '<button name="action" value="withdraw">Withdraw</button>'
        '</form>'
        f'<p style="color:red">{msg}</p>'
        f'<pre>{ledgers}</pre>'
        f'<pre>{chart}</pre>'
    )


if __name__ == '__main__':
    app.run(debug=True)
