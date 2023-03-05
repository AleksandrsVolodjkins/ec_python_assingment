import requests
import json
import csv
import crud





def menu():
    print("Welcome to the FastAPI menu!")
    print("0. Seed database")
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

# Set up base URLs for API endpoints
customers_url = 'http://localhost:8000/customers/'
items_url = 'http://localhost:8000/items/'
details_url = 'http://localhost:8000/details/'

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == "0":

            # Helper function to read data from CSV file and return as list of dictionaries
            def read_csv_data(filename):
                with open(filename, 'r') as f:
                    reader = csv.DictReader(f)
                    data = [row for row in reader]
                return data

            # Read customer data from CSV file and create customers via API calls
            customer_data = read_csv_data('data/customers.csv')
            for customer in customer_data:
                response = requests.post(customers_url, json=customer)
                if response.status_code == 200:
                    print(f"Customer created: {customer}")
                else:
                    print(f"Error creating customer {customer}: {response.status_code} - {response.content}")

            # Read item data from CSV file and create items via API calls
            item_data = read_csv_data('data/items.csv')
            for item in item_data:
                response = requests.post(items_url, json=item)
                if response.status_code == 200:
                    print(f"Item created: {item}")
                else:
                    print(f"Error creating item {item}: {response.status_code} - {response.content}")

            # Read detail data from CSV file and create details via API calls
            detail_data = read_csv_data('data/details.csv')
            for detail in detail_data:
                response = requests.post(details_url, json=detail)
                if response.status_code == 200:
                    print(f"Detail created: {detail}")
                else:
                    print(f"Error creating detail {detail}: {response.status_code} - {response.content}")
        if choice == "1":
            url = 'http://localhost:8000/customers/'
            headers = {'Content-Type': 'application/json'}

            # Ask for user input
            full_name = input('Enter full name: ')

            data = {
                'full_name': full_name,
            }

            response = requests.post(url, headers=headers, data=json.dumps(data))

            if response.status_code == 200:
                customer = json.loads(response.content)
                print(customer)
            else:
                print('Error:', response.status_code, response.reason)
        elif choice == "2":
            url = 'http://localhost:8000/customers/'
            params = {'skip': 0, 'limit': 10}

            response = requests.get(url, params=params)

            if response.status_code == 200:
                customers = json.loads(response.content)
                print(customers)
            else:
                print('Error:', response.status_code, response.reason)
        elif choice == "3":

            url = 'http://localhost:8000/customers/'
            customer_id = input('Enter customer id: ')

            response = requests.get(url + str(customer_id))

            if response.status_code == 200:
                customer = json.loads(response.content)
                print(customer)
            else:
                print('Error:', response.status_code, response.reason)


        elif choice == "4":
            url = 'http://localhost:8000/customers/'
            customer_id = input('Enter customer id: ')

            # Ask for user input
            full_name = input('Enter full name: ')

            data = {
                'full_name': full_name,
            }

            response = requests.put(url + str(customer_id), json=data)

            if response.status_code == 200:
                customer = json.loads(response.content)
                print('Updated customer:', customer)
            else:
                print('Error:', response.status_code, response.reason)
  
        elif choice == "5":

            url = 'http://localhost:8000/customers/'
            customer_id = input('Enter customer id: ')

            response = requests.delete(url + str(customer_id))

            if response.status_code == 200:
                print('Customer deleted successfully')
            else:
                print('Error:', response.status_code, response.reason)

           
        elif choice == "6":
            url = 'http://localhost:8000/items/'
            response = requests.get(url)

            if response.status_code == 200:
                items = json.loads(response.content)
                print('Items:', items)
            else:
                print('Error:', response.status_code, response.reason)
      
        elif choice == "7":
            url = 'http://localhost:8000/details/'
            response = requests.get(url)

            if response.status_code == 200:
                details = json.loads(response.content)
                print('Details:', details)
            else:
                print('Error:', response.status_code, response.reason)

        elif choice == "8":
            print("Exiting menu...")
            break
        else:
            print("Invalid choice! Please enter a number from 1-8.")