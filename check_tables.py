from sqlalchemy import create_engine, MetaData, Table

# Replace 'your_database_url' with your actual database URL
database_url = 'sqlite:///instance/mydatabase.db'

try:
    engine = create_engine(database_url)
    print("Database engine created successfully")

    meta = MetaData()
    meta.reflect(bind=engine)
    print("Metadata reflected successfully")

    for table_name in meta.tables.keys():
        table = Table(table_name, meta, autoload=True, autoload_with=engine)
        print(f"Table Name: {table_name}")
        print(f"Columns: {', '.join([column.name for column in table.c])}")

except Exception as e:
    print(f"An error occurred: {e}")


