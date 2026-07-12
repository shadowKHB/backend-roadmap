def main():
    def show_balance(balance):
        print(f"Your balance is ${balance:.2f}")


    def deposit():
        amount = float(input("Enter an amount to be deposited: "))

        if amount < 0:
            print("That's not a valid amount")
            return 0
        else:
            print(f"Deposit successful!") 
            return amount 
             


    def withdraw(balance):
        amount = float(input("Enter an amount to be withdrow: "))

        if amount > balance:
            print(f"Insufficient funds")
            return 0
        elif amount < 0:
            print("Amount must be greater than 0")
            return 0
        else:
            print("Withdrawal successful! Please collect your cash.")       
            return amount 
            
    balance = 0
    is_running = True

    while is_running:
        print("===== Banking Program =====")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("===========================")

        choice = int(input("Enter your choice(1-4): "))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running =False
        else:
            print("That is not a valid choice")    

    print("Thank you! See you later..")        

if __name__ == "__main__":
    main()