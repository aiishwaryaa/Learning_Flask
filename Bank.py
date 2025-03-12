from flask import Flask ,render_template
app = Flask(__name__)


class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited Rs.{amount}. New balance is Rs.{self.balance}."
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew Rs.{amount}. New balance is Rs.{self.balance}."
        return "Invalid amount entered."


account = BankAccount(1234567890033, 30000, "25-03-2024", "Aishwarya")

@app.route('/')
def home():
    return render_template('bank.html', account=account, message="")

@app.route('/deposit/<int:amount>')
def deposit(amount):
    message = account.deposit(amount)
    return render_template('bank.html', account=account, message=message)


@app.route('/withdraw/<int:amount>')
def withdraw(amount):
    message = account.withdraw(amount)
    return render_template('bank.html', account=account, message=message)

if __name__ == '__main__':
    app.run(debug=True)