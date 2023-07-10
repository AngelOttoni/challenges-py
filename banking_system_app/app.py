import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def perform_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)


class Person(Client):
    def __init__(self, name, birth_date, cpf, address):
        super().__init__(address)
        self.name = name
        self.birth_date = birth_date
        self.cpf = cpf


class Account:
    def __init__(self, number, client):
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._client = client
        self._history = History()

    @classmethod
    def new_account(cls, client, number):
        return cls(number, client)

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def agency(self):
        return self._agency

    @property
    def client(self):
        return self._client

    @property
    def history(self):
        return self._history

    def withdraw(self, amount):
        balance = self.balance
        exceeded_balance = amount > balance

        if exceeded_balance:
            print("\n@@@ Invalid operation! Your account does not have enough balance. @@@")

        elif amount > 0:
            self._balance -= amount
            print("\n=== Your withdrawal was successful! ===")
            return True

        else:
            print("\n@@@ Invalid operation! The entered value is invalid. @@@")

        return False

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("\n=== Your deposit was successful! ===")
        else:
            print("\n@@@ Invalid operation! The entered value is invalid. @@@")
            return False

        return True

#CONTA CORRENTE
class CheckingAccount(Account):
    def __init__(self, number, client, limit=500, max_withdrawals=3):
        super().__init__(number, client)
        self._limit = limit
        self._max_withdrawals = max_withdrawals
    #SACAR
    def withdraw(self, amount):
        #SAQUES
        withdrawals = len([transaction for transaction in self.history.transactions if transaction["type"] == Withdrawal.__name__])
        exceeded_limit = amount > self._limit
        exceeded_withdrawals = withdrawals >= self._max_withdrawals

        if exceeded_limit:
            print("\n@@@ Invalid operation! Withdrawal amount exceeds limit. @@@")

        elif exceeded_withdrawals:
            print("\n@@@ Invalid operation! Exceeded maximum number of withdrawals. @@@")

        else:
            return super().withdraw(amount)

        return False

    def __str__(self):
        return f"""\
            Agency:\t{self.agency}
            C/A:\t\t{self.number}
            Account Owner:\t{self.client.name}
        """


class History:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "amount": transaction.amount,
                "date": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transaction(ABC):
    @property
    @abstractproperty
    def amount(self):
        pass

    @abstractclassmethod
    def register(self, account):
        pass

#SAQUE
class Withdrawal(Transaction):
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def register(self, account):
        successful_transaction = account.withdraw(self.amount)

        if successful_transaction:
            account.history.add_transaction(self)


class Deposit(Transaction):
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def register(self, account):
        successful_transaction = account.deposit(self.amount)

        if successful_transaction:
            account.history.add_transaction(self)


def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDeposit
    [2]\tWithdraw
    [3]\tEstatement
    [4]\tNew client
    [5]\tNew account
    [6]\tList accounts
    [7]\tExit
    => """
    return input(textwrap.dedent(menu))


def filter_client(cpf, clients):
    filtered_clients = [client for client in clients if client.cpf == cpf]
    return filtered_clients[0] if filtered_clients else None

def retrieve_client_account(client):
    if not client.accounts:
        print("\n@@@ Client not found! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return client.accounts[0]


def deposit(clients):
    cpf = input("Enter the client's CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n@@@ Client not found! @@@")
        return

    amount = float(input("Enter the deposit amount: "))
    transaction = Deposit(amount)

    account = retrieve_client_account(client)
    if not account:
        return

    client.perform_transaction(account, transaction)


def withdraw(clients):
    cpf = input("Enter the client's CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n@@@ Client not found! @@@")
        return

    amount = float(input("Enter the withdrawal amount: "))
    transaction = Withdrawal(amount)

    account = retrieve_client_account(client)
    if not account:
        return

    client.perform_transaction(account, transaction)


def display_statement(clients):
    cpf = input("Enter the client's CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n@@@ Client not found! @@@")
        return

    account = retrieve_client_account(client)
    if not account:
        return

    print("\n================ STATEMENT ================")
    transactions = account.history.transactions

    statement = ""
    if not transactions:
        statement = "No transactions have been made."
    else:
        for transaction in transactions:
            statement += f"\n{transaction['type']}:\n\tR$ {transaction['amount']:.2f}"

    print(statement)
    print(f"\nBalance:\n\tR$ {account.balance:.2f}")
    print("==========================================")


def create_client(clients):
    cpf = input("Enter CPF (number only): ")
    client = filter_client(cpf, clients)

    if client:
        print("\n@@@ There is already a client with this CPF! @@@")
        return

    name = input("Enter the client's name: ")
    birth_date = input("Enter the client's date of birth (dd-mm-yyyy): ")
    address = input("Enter the client's address: ")

    client = Person(name=name, birth_date=birth_date, cpf=cpf, address=address)

    clients.append(client)

    print("\n=== Client created successfully! ===")


def create_account(account_number, clients, accounts):
    cpf = input("Enter the client's CPF: ")
    client = filter_client(cpf, clients)

    if not client:
        print("\n@@@ Client not found, account creation flow closed! @@@")
        return

    account = CheckingAccount.new_account(client=client, number=account_number)
    accounts.append(account)
    client.accounts.append(account)

    print("\n=== Account created successfully! ===")


def list_accounts(accounts):
    for account in accounts:
        print("=" * 100)
        print(textwrap.dedent(str(account)))


def main():
    clients = []
    accounts = []

    while True:
        option = menu()

        if option == "1":
            deposit(clients)

        elif option == "2":
            withdraw(clients)

        elif option == "3":
            display_statement(clients)

        elif option == "4":
            create_client(clients)

        elif option == "5":
            number_account = len(accounts) + 1
            create_account(number_account, clients, accounts)

        elif option == "6":
            list_accounts(accounts)

        elif option == "7":
            break

        else:
            print("\n@@@ Invalid operation! Please select a valid operation. @@@")
main()