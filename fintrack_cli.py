import json
from pathlib import Path

DATA_FILE = Path("fintrack_data.json")


def load_expenses():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense(expenses):
    print("\n--- Add Expense ---")
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    category = input("Category (food, travel, bills, etc.): ").strip().lower()
    note = input("Note (optional): ").strip()

    expense = {
        "amount": amount,
        "category": category,
        "note": note
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("✔ Expense added!")


def list_expenses(expenses):
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    for i, e in enumerate(expenses, start=1):
        line = f"{i}. ₹{e['amount']} - {e['category']}"
        if e['note']:
            line += f" ({e['note']})"
        print(line)


def summary(expenses):
    print("\n--- Summary by Category ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]

    for cat, total in totals.items():
        print(f"{cat}: ₹{total:.2f}")
    print(f"\nTotal: ₹{sum(totals.values()):.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n==== FinTrack CLI ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            summary(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
