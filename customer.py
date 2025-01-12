import sqlite3


class Customer:
    def __init__(self, customer_id, fname, lname, address, mobile):
        self.customer_id = customer_id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.mobile = mobile

    def __repr__(self):
        return f"Customer({self.customer_id}, {self.fname}, {self.lname}, {self.address}, {self.mobile})"

    def __eq__(self, other):
        if not isinstance(other, self.customer_id):
            return False
        return (
            self.customer_id == other.customer_id and
            self.fname == other.fname and
            self.lname == other.lname and
            self.address == other.address and
            self.mobile == other.mobile
        )

    def __ne__(self, other):
        if not isinstance(other, self.customer_id):
            return True
        return (
            self.customer_id != other.customer_id and
            self.fname != other.fname and
            self.lname != other.lname and
            self.address != other.address and
            self.mobile != other.mobile
        )

    def __hash__(self):
        return hash((self.customer_id, self.fname, self.lname, self.address, self.mobile))


# Table creation logic
def create_table():
    conn = sqlite3.connect("hwoop2.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer (
	        customer_id INTEGER PRIMARY KEY,
            fname varchar,
	        lname varchar,
	        address varchar,
            mobile INTEGER
        );
    """)
    conn.commit()
    conn.close()


# Ensure the table is created only when this script is run directly
if __name__ == "__main__":
    create_table()

import sqlite3

conn = sqlite3.connect("hwoop2.db")
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(customer);")
print(cursor.fetchall())
conn.close()
