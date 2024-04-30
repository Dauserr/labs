import csv
import psycopg2
from config import load_config

def create_table(conn):
    """ Connect to the PostgreSQL database server """
    try:
        #cursor object creating
        cur = conn.cursor()

        #creating table
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                Name VARCHAR(100),
                Phone_number VARCHAR(20),
                EMail VARCHAR(100),
                Address VARCHAR(150)
            );
        '''

        #execute to create
        cur.execute(create_table_query)

        # Commit
        conn.commit()

        print("table created")

    except (psycopg2.DatabaseError, Exception) as error:
        print("error while creating table: ", error)
    finally:
        # close the cursor
        if cur:
            cur.close()

def insert_data(conn, name, phone_number, email,address):
    #inserting
    try:
        #cursor object creating
        cur = conn.cursor()

        insert_query = """
            INSERT INTO phonebook (Name, Phone_number, EMail, Address)
            VALUES (%s,%s,%s,%s)
        """
        #%s to insert
        data = (name,phone_number,email,address)

        cur.execute(insert_query, data)

        conn.commit()

        print("Data inserted")

    except (psycopg2.DatabaseError, Exception) as error:
        print("error while inserting data: ", error)
    finally:
        # close the cursor
        if cur:
            cur.close()

def update_data(conn, id, new_name,new_phone_number, new_email, new_address):
    #updating
    try:
        #cursor object creating
        cur = conn.cursor()

        update_query = """
            UPDATE phonebook
            SET Name = %s, Phone_number = %s, EMail = %s, Address = %s
            WHERE id = %s;
        """
        data = (new_name, new_phone_number, new_email, new_address, id)

        cur.execute(update_query, data)

        conn.commit()

        print("Data updated")
    except (psycopg2.DatabaseError, Exception) as error:
        print("error while updating data: ", error)
    finally:
        # close the cursor
        if cur:
            cur.close()

def query_data(conn, filter=None):
    #query data

    try:
        #cursor object creating
        cur = conn.cursor()

        if filter:
            query = f"SELECT * FROM phonebook WHERE {filter};"
        else:
            query = "SELECT * FROM phonebook;"

        cur.execute(query)

        #все строки в rows
        rows = cur.fetchall()

        for row in rows:
            print(row)

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while querying data: ", error)
    finally:
        if cur:
            cur.close()

def delete_data(conn, condit):
    #deleting data
    try:
        #cursor object creating
        cur = conn.cursor()

        query = f"DELETE FROM phonebook WHERE {condit};"

        cur.execute(query)

        conn.commit()

        print("Data deleted")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while deleting data: ", error)
    finally:
        if cur:
            cur.close()

def creupd(conn, name, phone_number, email,address):
    try:
        #cursor object creating
        cur = conn.cursor()

        query = "SELECT EXISTS(SELECT 1 FROM phonebook WHERE name = %s);"

        cur.execute(query, (name,)) # need tuple then i used comma
        name_exists = cur.fetchone()[0]

        if name_exists:
            cur.execute("SELECT id FROM phonebook WHERE name = %s;", (name,))
            id = cur.fetchone()[0]
            update_data(conn,id, name, phone_number, email,address)
        else:
            insert_data(conn, name, phone_number, email,address)
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while inserting or updating data: ", error)
    finally:
        if cur:
            cur.close()

def many(conn, name, phone_number, email,address):
    try:
        #cursor object creating
        cur = conn.cursor()
        if len(phone_number)==12:
            creupd(conn, name, phone_number, email,address)
        else:
            print("The phone number is incorrect! ")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while inserting or updating many data: ", error)
    finally:
        if cur:
            cur.close()

if __name__ == '__main__':
    config = load_config()

    try:
        conn = psycopg2.connect(**config)
        print("connected to the postgresql server")

        #upd or ins
        #creupd(conn,"Serikbayev Daulet","+77772030403","d_serikbayev@kbtu.kz","32 makataeva st")


        #many times upd
        #n = int(input("how many times you want to add? "))
        #for i in range(0,n):
        #    many(conn,input("Name: "),input("email: "),input("phone number: "),input("address: "))
        #    n+=1


        #records based on a pattern
        #query_data(conn, "Name = 'Serikbayev Daulet'")

        #delete by name or phone
        #delete_data(conn, "name = Daulet Serikbayev") or "phone number = +77772030403"



    except (psycopg2.DatabaseError, Exception) as error:
        print("error while connecting to the postgresql server: ", error)
    finally:
        # close the db connection
        if conn:
            conn.close()
            print("connection closed.")
