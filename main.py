import duckdb

def main():
    # Your DuckDB code here
    connection = duckdb.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE test (id INTEGER, name VARCHAR)")
    cursor.execute("INSERT INTO test VALUES (1, 'DuckDB')")
    result = cursor.execute("SELECT * FROM test").fetchall()
    print(result)

if __name__ == "__main__":
    main()
