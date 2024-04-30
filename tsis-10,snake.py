import psycopg2
from config import load_config

def create_table(conn):
    """ Connect to the PostgreSQL database server """
    try:
        #cursor object creating
        cur = conn.cursor()

        #creating table
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS user_score (
                id SERIAL PRIMARY KEY,
                Username VARCHAR(100),
                Score VARCHAR(20),
                Level VARCHAR(20)
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

def delete_data(conn, condit):
    #deleting data
    try:
        #cursor object creating
        cur = conn.cursor()

        query = f"DELETE FROM user_score WHERE {condit};"

        cur.execute(query)

        conn.commit()

        print("Data deleted")

    except (psycopg2.DatabaseError, Exception) as error:
        print("Error while deleting data: ", error)
    finally:
        if cur:
            cur.close()


if __name__ == '__main__':
    config = load_config()

    try:
        conn = psycopg2.connect(**config)
        print("connected to the postgresql server")

        #since table is created, then i will comment the line
        #create_table(conn)
        #delete_data(conn, "id = 7")


    except (psycopg2.DatabaseError, Exception) as error:
        print("error while connecting to the postgresql server: ", error)
    finally:
        # close the db connection
        if conn:
            conn.close()
            print("connection closed.")
