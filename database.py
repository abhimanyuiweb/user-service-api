# database.py
import psycopg2


def get_connection():
    conn = psycopg2.connect(
        dbname="fast_api_demo",
        user="fastapi_user",
        password="Anamika@#@#2004",
        host="localhost",
        port="5432"
    )

    return conn


# Create a cursor to execute SQL commands
# cur = conn.cursor()


# Example: create a table
# cur.execute(
#     "CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(50));")

# Example: insert data
# cur.execute(
    # "INSERT INTO cars (brand, model, year, color) VALUES ('Mahindra', 'Scorpio N', 2018, 'Green')")

# Example: fetch data
# cur.execute("SELECT * FROM cars;")
# rows = cur.fetchall()
# for row in rows:
#     print(row)


# Save changes
# conn.commit()

# Close cursor and connection
# cur.close()
# conn.close()
