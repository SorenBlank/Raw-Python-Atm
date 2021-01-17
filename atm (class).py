import time
class bank:
    def __init__(self):
        self.id = 1000
    def system(self):
        while True:
            #Line 8 to 13 is for only asking an input
            print("What you want to Do?")
            print("1/ Withdraw")
            print("2/ Deposit")
            print("3/ Balance Check")
            print("4/ Exit")
            print("Type down the number")
            #Line 15 is for taking input from user as an integer
            self.ask = int(input())
            #Line 17 will break the loop if user's input is equal to 4
            if self.ask == 4:
                break
            if self.ask == 1:
                print("Balance:", self.id)
                question = int(input("How much money you want to withdraw: "))
                if question < self.id:
                    print("Please wait: ")
                    time.sleep(5)
                    self.id = self.id - question
                    print()
                    print()
                    print("Transection Completed")
                    print("Current Balance:", self.id)
                    print()
                    print()
                else:
                    print("System Failed Try Again")
            if self.ask == 2:
                print("Balance:", self.id)
                question2 = int(input("How much money you want to deposit: "))
                if question2 > 200:
                    print("Please wait: ")
                    self.id = self.id + question2
                    time.sleep(2)
                    print("Transection Completed")
                    print("Current Balance:", self.id)
                    print()
                    print()
                else:
                    print("You can not deposit less than 200")
            if self.ask == 3:
                print()
                print()
                print("Your current balance is:",self.id)
                print()
                print()

my_account = bank()
my_account.system()