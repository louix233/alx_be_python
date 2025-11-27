import sys
from bank_account import BankAccount

def main()
    # Create an account with a starting balance of 100
    account = BankAccount(100)

    if len(sys.argv)  2
        print(Usage python main-0.py commandamount)
        print(Commands deposit, withdraw, display)
        sys.exit(1)

    # Split the command and optional amount
    command, params = sys.argv[1].split('')
    amount = float(params[0]) if params else None

    # Handle deposit command
    if command == deposit and amount is not None
        account.deposit(amount)
        print(fDeposited ${amount})

    # Handle withdraw command
    elif command == withdraw and amount is not None
        if account.withdraw(amount)
            print(fWithdrew ${amount})
        else
            print(Insufficient funds.)

    # Handle display command
    elif command == display
        account.display_balance()

    else
        print(Invalid command.)

if __name__ == __main__
    main()
