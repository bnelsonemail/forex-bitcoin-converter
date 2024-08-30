import os

# Define paths
table_file_path = '/mnt/d/Users/Bnelson/NewHome/computer_science/USF_Bootcamp/3_core/projects/22.3_forex/static/table.htm'
tables_file_path = 'templates/tables.html'

# Check if the table.html file exists
if not os.path.exists(table_file_path):
    print(f"Error: The file {table_file_path} does not exist.")
else:
    # Read the table.html content
    with open(table_file_path, 'r') as file:
        table_content = file.read()

    # Check if the tables.html file exists
    if not os.path.exists(tables_file_path):
        print(f"Error: The file {tables_file_path} does not exist.")
    else:
        # Read the tables.html content
        with open(tables_file_path, 'r') as file:
            tables_content = file.read()

        # Define the placeholder where you want to insert the table in tables.html
        placeholder = 'currency_table'

        # Insert the table content at the placeholder
        new_tables_content = tables_content.replace(placeholder, table_content)

        # Write the new content back to the tables.html file
        with open(tables_file_path, 'w') as file:
            file.write(new_tables_content)

        print("Table has been successfully added to the tables.html file.")


