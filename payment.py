# Simple Payment App 

import time

# Sample database 
users = {
    "alice" :  {"pin": "1234", "balance": 5000, "history": []},
    "bob"   :  {"pin": "5678", "balance": 5000, "history": []},
    "ganesh":  {"pin": "1221", "balance": 5000, "history": []},
    "guru"  :  {"pin": "8967", "balance": 5000, "history": []},
    "shashi":  {"pin": "9876", "balance": 5000, "history": []},
    "abhi"  :  {"pin": "1254", "balance": 5000, "history": []},
    "vikas" :  {"pin": "1284", "balance": 5000, "history": []},
    "dhanu" :  {"pin": "1534", "balance": 5000, "history": []},
    "gani"  :  {"pin": "1345", "balance": 5000, "history": []},
    "srujan":  {"pin": "8765", "balance": 5000, "history": []},
    "sidd"  :  {"pin": "9878", "balance": 5000, "history": []},
    "bharth":  {"pin": "3677", "balance": 5000, "history": []},
    "sadya" :  {"pin": "8753", "balance": 5000, "history": []},
    "raghu" :  {"pin": "4565", "balance": 5000, "history": []},
    "ravi"  :  {"pin": "3221", "balance": 5000, "history": []},
}

def show_menu(username):
    print(f"\nWelcome, {username.title()}!")
    print("1. Check Balance")
    print("2. Send Money")
    print("3. View Transaction History")
    print("4. Logout")

def check_balance(username):
    print(f"\n💰 Your current balance: ₹{users[username]['balance']}")

def send_money(sender):
    receiver = input("Enter receiver username: ").lower()
    if receiver not in users:
        print("❌ User not found!")
        return
    try:
        amount = float(input("Enter amount to send: ₹"))
    except ValueError:
        print("❌ Invalid amount!")
        return

    if amount <= 0:
        print("❌ Enter a positive amount!")
        return

    if users[sender]["balance"] < amount:
        print("⚠️ Insufficient balance!")
        return

    users[sender]["balance"] -= amount
    users[receiver]["balance"] += amount
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Save transaction history
    users[sender]["history"].append(f"Sent ₹{amount} to {receiver} on {timestamp}")
    users[receiver]["history"].append(f"Received ₹{amount} from {sender} on {timestamp}")

    print(f"✅ Transaction successful! You sent ₹{amount} to {receiver}.")

def view_history(username):
    print("\n📜 Transaction History:")
    if not users[username]["history"]:
        print("No transactions yet.")
    else:
        for record in users[username]["history"]:
            print("-", record)

def login():
    username = input("Enter username: ").lower()
    pin = input("Enter 4-digit PIN: ")

    if username in users and users[username]["pin"] == pin:
        print("✅ Login successful!")
        return username
    else:
        print("❌ Invalid username or PIN.")
        return None

def main():
    print("================= Welcome to PaySim🏧 ===============")
    while True:
        print("\n1.Login")
        print("2.Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            user = login()
            if user:
                while True:
                    show_menu(user)
                    option = input("Enter choice: ")

                    if option == "1":
                        check_balance(user)
                    elif option == "2":
                        send_money(user)
                    elif option == "3":
                        view_history(user)
                    elif option == "4":
                        print("👋 Logged out successfully.")
                        break
                    else:
                        print("❌ Invalid option. Try again.")
        elif choice == "2":
            print("🚪 Exiting...\n Thank you for using PaySim..!")
            break
        else:
            print("❌ Invalid input, try again.")

if __name__ == "__main__":
    main()
