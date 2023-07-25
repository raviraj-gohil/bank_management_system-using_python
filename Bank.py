# bank management system

import random

customer = {
    1212121212 : {
    'name': 'ravi',
    'age': 23,
    'gender': 'male',
    'adhar': 123456789123,
    'password': 'okok',
    'balance': 2000
    }
}
# -------------------------------------------------------------------------

def exist_cust(customer):
    flag = 0
    while True:
        if flag == 0:
            try:
                account = int(input("Enter A/C number - "))
                if account in customer:
                    flag = 1
                else:
                    raise ValueError("This A/C number is not Exist")

            except ValueError as e:
                print("Error :", str(e))
        if flag == 1:
            try:
                password = input("Enter password - ")
                if password == customer[account]['password']:
                    break
                else:
                    raise ValueError("Wrong Password!")
            except ValueError as e:
                print("Error :", str(e))

    customer_name = customer[account].get('name')
    print(f"\nHello {customer_name}\nWelcome to The Uchiha Bank")
    operations(customer, account)

# ----------------------------------------------------------------------------

def operations(cutomer, account):
    Account = account
    print("\n\t1 for Add Amount\n\t2 for Withdrawal\n\t3 for Check Balance\n\t4 for Main Menu")
    while True:
        choice = int(input("Enter your choice - "))
        if choice == 1:
            credit(customer, account)
            break
        elif choice == 2:
            debit(customer, account)
            break
        elif choice == 3:
            print("\nYour Balance is", customer[Account]['balance'])
            while True:
                print("\n\t1 for Back\n\t2 for Main Menu")
                choice = int(input("Enter choice - "))
                if choice == 1:
                    operations(customer, account)
                    break
                elif choice == 2:
                    bank()
                    break
        elif choice == 4:
            bank()
            break

# ----------------------------------------------------------------------------

def new_customer():
    print("\n\t---Enter Your Details---\n")
    flag = 0
    while True:
        if flag == 0:
            name = input("Name - ")
            flag = 1
        if flag == 1:
            try:
                age = int(input("Age - "))
                if age:
                    pass
                else:
                    raise ValueError("Enter valid AGE")
                flag = 2
            except ValueError as e:
                print("Error :", str(e))
        if flag == 2:
            print("1 for MALE\n2 for FEMALE")
            try:
                gender_choice = int(input("Gender - "))
                if gender_choice == 1:
                    gender = 'male'
                    flag = 3
                elif gender_choice == 2:
                    gender = 'female'
                    flag = 3
                else:
                    raise ValueError("Please.. Enter valid choice")
            except ValueError as e:
                print("Error :", str(e))
        if flag == 3:
            try:
                adhar_no = int(input("Adhar number - "))
                adhar_len = str(adhar_no)
                if len(adhar_len) == 12:
                    adhar = adhar_no
                    flag = 4
                else:
                    raise ValueError("Enter 12 digit number only")
            except ValueError as e:
                print("Error :", str(e))
        if flag == 4:
            account_no = random.randint(1000000000, 9999999999)
            password = input("password - ")
            flag = 5
            print(f"Hello {name}\nWelcome to the UCHIHA bank\nYOUR ACCOUNT NUMBER IS",account_no)
            print("So based on our policy.. You have to deposit some Amount [ Minimum 2000 ] - ")
        if flag == 5:
            try:
                balance = int(input("Enter Amount here - "))
                if balance >= 2000:
                    customer[account_no] = {'name': name, 'age': age, 'gender': gender, 'adhar': adhar, 'password': password,
                                    'balance': balance}
                    print(f"ok Thanks {name} now your balance is {balance}")
                    break
                else:
                    raise ValueError("Enter Minimum 2000")
            except ValueError as e:
                print("Error :", str(e))
    while True:
        print("\n1 for back\n2 for exit")
        choice = int(input("Enter your choice - "))
        if choice == 1:
            bank()
            break
        elif choice == 2:
            print("Thank You For Visit.")
            break
        else:
            print("Please.. Enter valid choice")

# ----------------------------------------------------------------------------

def credit(customer, account):
    Amount = customer[account]['balance']
    Money = int(input("Add Money - "))
    if Money:
        Amount += Money
        print(f"{Money} credited to your A/C {account}")
    else:
        print("Please.. Enter valid input")

    customer[account].update(({'balance': Amount}))
    while True:
        print("\n\t1 for Back\n\t2 for Main Menu")
        choice = int(input("Enter choice - "))
        if choice == 1:
            operations(customer, account)
            break
        elif choice == 2:
            bank()
            break

# ----------------------------------------------------------------------------

def debit(cutomer, account):
    Amount = customer[account]['balance']
    Money = int(input("Enter Withdrawal Money - "))
    if Money:
        Amount -= Money
        if Amount < 2000:
            print("You dont have enough balace")
        else:
            customer[account].update(({'balance': Amount}))
            print(f"{Money} debited to your A/C {account}")
    else:
        print("Please.. Enter valid input")

    while True:
        print("\n\t1 for Back\n\t2 for Main Menu")
        choice = int(input("Enter choice - "))
        if choice == 1:
            operations(customer, account)
            break
        elif choice == 2:
            bank()
            break

# ----------------------------------------------------------------------------

def bank():
    print("\n\t---UCHIHA BANK---")
    while True:
        print("\n1 for new customer\n2 for exist customer\n3 for exit")
        choice = int(input("Enter your choice - "))
        if choice == 1:
            new_customer()
            break

        elif choice == 2:
            exist_cust(customer)
            break

        elif choice == 3:
            print("\nThank You For Visit..")
            break

        else:
            print("PLease.. Enter valid choice !")

# ----------------------------------------------------------------------------

bank()
