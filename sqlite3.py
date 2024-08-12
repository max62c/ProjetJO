import sqlite3
from sqlite3 import Error

class OlympicDatabase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        self.create_connection()
        self.create_table()

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            print(f"Connected to SQLite database: {self.db_file}")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_table(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS olympic_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event TEXT NOT NULL,
            gold TEXT NOT NULL,
            silver TEXT NOT NULL,
            bronze TEXT NOT NULL,
            year INTEGER NOT NULL
        );
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(create_table_sql)
            self.conn.commit()
        except Error as e:
            print(f"Error creating table: {e}")

    def insert_results(self, results_df, year):
        insert_sql = """
        INSERT INTO olympic_results (event, gold, silver, bronze, year)
        VALUES (?, ?, ?, ?, ?)
        """
        try:
            cursor = self.conn.cursor()
            for _, row in results_df.iterrows():
                cursor.execute(insert_sql, (row['event'], row['gold'], row['silver'], row['bronze'], year))
            self.conn.commit()
            print(f"Inserted {len(results_df)} records for year {year}")
        except Error as e:
            print(f"Error inserting records: {e}")

    def fetch_results(self, year=None):
        if year:
            select_sql = "SELECT * FROM olympic_results WHERE year = ?"
            params = (year,)
        else:
            select_sql = "SELECT * FROM olympic_results"
            params = ()

        try:
            cursor = self.conn.cursor()
            cursor.execute(select_sql, params)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Error fetching results: {e}")
            return []

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed")

# Example usage:
# db = OlympicDatabase("olympic_results.db")
# db.insert_results(results_df, 2020)
# results = db.fetch_results(2020)
# db.close_connection()