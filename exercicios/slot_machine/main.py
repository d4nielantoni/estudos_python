import random
from colorama import Fore, Style, init


init(autoreset=True) # Iniciando colorama, aqui usei só para mudar a cor ao executar o código

def spin_row():
    symbols = ["🍒", "💎", "🍊", "🍋", "🍉"]
    row = [random.choice(symbols) for _ in range(3)]
    return row

def print_row(row):
    print(" ".join(row))

def get_payout(row):
    payout = 0
    if row.count("🍒") == 3:
        payout = 10
    elif row.count("💎") == 3:
        payout = 20
    elif row.count("🍊") == 3:
        payout = 30
    elif row.count("🍋") == 3:
        payout = 40
    elif row.count("🍉") == 3:
        payout = 50
    return payout

def main():
    balance = 100

    print(Fore.GREEN + "************************************")
    print(Fore.GREEN + "Welcome to the Python Slot Machine!")
    print("Symbols: 🍒  💎  🍊  🍋  🍉")

    row = spin_row()
    print_row(row)
    payout = get_payout(row)
    balance += payout
    print(Fore.GREEN + "Payout:", payout)
    print(Fore.GREEN + "Balance:", balance)

main()

#oi