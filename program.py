import sqlite3
from customer import Customer

conn = sqlite3.connect("hwoop2.db")
cursor = conn.cursor()


def print_all_customers():
    conn = sqlite3.connect("hwoop2.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Customer")
    rows = cursor.fetchall()
    conn.close()
    customers = [Customer(*row) for row in rows]
    for customer in customers:
        print(customer)


if __name__ == "__main__":
    print_all_customers()


def insert_customer():
    while True:
        first_name_input = input("First Name: ")
        last_name_input = input("Last Name: ")
        address_input = input("Address: ")
        mobile_input = int(input("Mobile: "))

        # Create a Customer object (assuming `customer_id` is auto-incremented)
        customer_insert = Customer(None, first_name_input, last_name_input, address_input, mobile_input)

        # Connect to the database and insert the customer
        conn = sqlite3.connect("hwoop2.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO customer (fname, lname, address, mobile)
            VALUES (?, ?, ?, ?)
        """, (customer_insert.fname, customer_insert.lname, customer_insert.address, customer_insert.mobile))
        conn.commit()
        conn.close()
        break


insert_customer()
