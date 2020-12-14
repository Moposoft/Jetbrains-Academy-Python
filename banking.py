from random import randint
import sqlite3


class Account:

    def __init__(self):
        self.pin_code = "".join(map(str, [randint(0, 9) for _ in range(4)]))
        self.card_number = self.generate_card_number()
        self.balance = 0

    def generate_card_number(self):
        iin = "400000"
        while True:
            new_number = iin + "".join(map(str, [randint(0, 9) for _ in range(9)]))
            checksum = luhn_algorithm(new_number)
            new_number = new_number + checksum
            cur.execute("select number from card where number = ? ", (int(new_number),))
            if cur.fetchone() is None:
                cur.execute("insert into card(number, pin) values(?, ?)", [new_number, self.pin_code])
                conn.commit()
                return new_number


def luhn_algorithm(card_number):
    luhn = [int(x) * 2 if i % 2 == 0 else int(x) for i, x in enumerate(card_number)]
    luhn = sum([x - 9 if x > 9 else x for x in luhn])
    checksum = 10 - luhn % 10 if not luhn % 10 == 0 else 0
    return str(checksum)


def manage_account(card_number):
    while True:
        print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
        cur.execute("select balance from card where number = ?", (card_number,))
        balance = cur.fetchone()[0]
        user_input = input()
        if user_input == "0":
            print("Bye!")
            exit()
        elif user_input == "1":
            print("Balance: " + str(balance))
        elif user_input == "2":
            print("Enter income:")
            balance += int(input())
            cur.execute("update card set balance = ? where number = ?", [balance,card_number])
            conn.commit()
            print("Income was added!:")
        elif user_input == "3":
            print("Transfer")
            print("Enter card number:")
            card_number2 = input()
            if int(card_number2[-1]) != int(luhn_algorithm(card_number2[:-1])):
                print("Probably you made a mistake in the card number. Please try again!")
            else:
                cur.execute("select balance from card where number = ?", (card_number2,))
                balance2 = cur.fetchone()
                if balance2 is None:
                    print("Such a card does not exist.")
                else:
                    print("Enter how much money you want to transfer:")
                    transfer = int(input())
                    if transfer > balance:
                        print("Not enough money!")
                    else:
                        balance -= transfer
                        balance2 = balance2[0] + transfer
                        cur.execute("update card set balance = ? where number = ?", [balance,card_number])
                        conn.commit()
                        cur.execute("update card set balance = ? where number = ?", [balance2,card_number2])
                        conn.commit()
                        print("Success!")

        elif user_input == "4":
            cur.execute("delete from card where number = ?", (card_number,))
            conn.commit()
            print("The account has been closed!")
            return
        elif user_input == "5":
            print("You have successfully logged out!")
            return


conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
cur.execute("create table if not exists card(id INTEGER, number TEXT, pin TEXT, balance INTEGER default 0);")
conn.commit()
while True:
    print("1. Create an account\n2. Log into account\n0. Exit")
    user_input = input()
    if user_input == "0":
        print("Bye!")
        break
    elif user_input == "1":
        new_account = Account()
        print("Your card has been created\nYour card number:")
        print(new_account.card_number)
        print("Your card PIN:")
        print(new_account.pin_code)
    elif user_input == "2":
        print("Enter your card number:")
        card_number = input()
        print("Enter your PIN:")
        pin_code = input()
        cur.execute("select * from card where number = ? and pin = ?", [card_number, pin_code])
        if cur.fetchone() is not None:
            print("You have successfully logged in!")
            manage_account(card_number)
        else:
            print("Wrong card number or PIN!")
conn.close()
