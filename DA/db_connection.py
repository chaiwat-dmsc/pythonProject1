import pyodbc

class SQLServerExporter:
    def __init__(self, server, database):
        self.server = server
        self.database = database
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            conn_str = f"DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;"
            self.conn = pyodbc.connect(conn_str)
            self.cursor = self.conn.cursor()
        except pyodbc.Error as e:
            print("An error occurred while connecting to the database: " + str(e))

    def disconnect(self):
        try:
            self.cursor.close()
            self.conn.close()
        except pyodbc.Error as e:
            print("An error occurred while disconnecting from the database: " + str(e))

    def get_table_names(self):
        table_query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"
        try:
            self.cursor.execute(table_query)
            tables = [row[0] for row in self.cursor.fetchall()]
            return tables
        except pyodbc.Error as e:
            print("An error occurred while fetching table names: " + str(e))

    def get_column_names(self, table_name):
        column_query = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'"
        try:
            self.cursor.execute(column_query)
            columns = [row[0] for row in self.cursor.fetchall()]
            return columns
        except pyodbc.Error as e:
            print("An error occurred while fetching column names: " + str(e))

    def print_table_and_column_names(self):
        tables = self.get_table_names()
        for table in tables:
            column_names = self.get_column_names(table)
            if not column_names:
                print(f"No columns found for table: {table}")
                continue
            print(f"Table name: {table}")
            print(f"Column names:", ", ".join(column_names))
            print("=" * 50)


if __name__ == "__main__":
    exporter = SQLServerExporter("Raji", "master")
    exporter.print_table_and_column_names()
    exporter.disconnect()

