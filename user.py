from cgi import print_arguments
from operator import truediv

from bankAccount import BankAccount

class User:
    def __init__(self, first_name, last_name, email, age,is_rewards_member=False,gold_card_points=0):
        self.first_name=first_name
        self.last_name= last_name
        self.email=email
        self.age= age
        self.account= BankAccount(int_rate=0.02, balance=0)

        # include as default attributes
        self.is_rewards_member= is_rewards_member
        self.gold_card_points= gold_card_points

# include these methods
    def display_info(self):# Have this method print all of the users' details on separate lines.
        print (f"{self.first_name} {self.last_name} {self.email} {self.age} {self.is_rewards_member} {self.gold_card_points}")

    def enroll(self):# Have this method change the user's member status to True and set their gold card points to 200.
        self.is_rewards_member= True
        self.gold_card_points= 200
        print (f'{self.gold_card_points} {self.is_rewards_member}')

    def spend_points(self, amount):
    # have this method decrease the user's points by the amount specified
        self.gold_card_points-= amount
        print (self.gold_card_points)


# add a make_deposit method
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print (self.account.balance)

#add a make_withdraw method
    def make_withdraw (self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)


#add a display_user_balance that displays user acc balance
    def display_user_balance (self):
        self.account.display_account_info
        print (self.account.display_account_info)


# sample user
user1=User("Tom", "leaf","blah@blah.com",30)
user1.enroll()
# user1.spend_points(100)
user1.display_info()
user1.make_deposit(50)
user1.make_withdraw(30)
user1.display_user_balance()
