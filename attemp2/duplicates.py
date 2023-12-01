import csv
from collections import defaultdict

def remove_duplicates_and_save(tsv_file, column_name, output_file):
    try:
        with open(tsv_file, 'r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file, delimiter='\t')

            # Create a defaultdict to track rows by the specified column
            rows_by_column = defaultdict(list)

            # Iterate through the rows and store them in the defaultdict
            for row in reader:
                column_value = row[column_name]
                rows_by_column[column_value].append(row)

            # Create a new list with only the first occurrence of each value in the specified column
            unique_rows = [rows[0] for rows in rows_by_column.values()]

        # Write the unique rows to a new TSV file
        with open(output_file, 'w', encoding='utf-8', newline='') as output_file:
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(output_file, delimiter='\t', fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(unique_rows)

    except FileNotFoundError:
        print(f"File '{tsv_file}' not found.")

if __name__ == "__main__":
    # Replace these values with the actual paths and column name
    input_tsv_file = 'annotated_data2.tsv'
    output_tsv_file = 'file_no_duplicates.tsv'
    column_to_check = 'title'

    # Remove duplicates and save to a new file
    remove_duplicates_and_save(input_tsv_file, column_to_check, output_tsv_file)

    print(f"Unique rows saved to: {output_tsv_file}")
