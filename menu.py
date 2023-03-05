from crud import create_customer, read_users, read_user, update_customer, delete_customer, read_items, read_details
from schemas import CustomerCreate
from fastapi import HTTPException





def menu():
    print("Welcome to the FastAPI menu!")
    print("1. Create a new customer")
    print("2. Read all customers")
    print("3. Read a specific customer")
    print("4. Update a customer")
    print("5. Delete a customer")
    print("6. Read all items")
    print("7. Read all details")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")
    return choice


if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == "1":
            full_name = input("Enter customer's full name: ")
            email = input("Enter customer's email address: ")
            new_customer = schemas.CustomerCreate(full_name=full_name, email=email)
            try:
                created_customer = create_customer(new_customer)
                print("Customer created successfully!")
                print(created_customer)
            except HTTPException as e:
                print(f"Error: {e.detail}")
        elif choice == "2":
            try:
                customers = read_users()
                print(customers)
            except HTTPException as e:
                print(f"Error: {e.detail}")
        elif choice == "3":
            customer_id = int(input("Enter customer ID: "))
            try:
                customer = read_user(customer_id)
                print(customer)
            except HTTPException as e:
                print(f"Error: {e.detail}")
        elif choice == "4":
            customer_id = int(input("Enter customer ID: "))
            full_name = input("Enter customer's full name: ")
            email = input("Enter customer's email address: ")
            updated_customer = schemas.CustomerCreate(full_name=full_name, email=email)
            try:
                updated = update_customer(customer_id, updated_customer)
                print("Customer updated successfully!")
                print(updated)
            except HTTPException as e:
                print(f"Error: {e.detail}")
        elif choice == "5":
            customer_id = int(input("Enter customer ID: "))
            try:
                deleted = delete_customer(customer_id)
                print("Customer deleted successfully!")
            except HTTPException as e:
                print(f"Error: {e.detail}")
        elif choice == "6":
            try:
                items = read_items()
                print(items)
            except HTTPException as e:
                print(f"Error: {e.detail}")
        elif choice == "7":
            try:
                details = read_details()
                print(details)
            except HTTPException as e:
                print(f"Error: {e.detail}")
        elif choice == "8":
            print("Exiting menu...")
            break
        else:
            print("Invalid choice! Please enter a number from 1-8.")