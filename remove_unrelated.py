import pandas as pd

def remove_unrelated_rows(input_file, output_file):

    df = pd.read_csv(input_file, sep='\t',header=None)

    
    df_filtered = df[df[2] != 'unrelated']

   
    df_filtered.to_csv(output_file, sep='\t', index=False)

if __name__ == "__main__":
    input_file = 'Data1130.tsv'  # Replace with your input file path
    output_file = 'removed_unrelated.tsv'  # Replace with your desired output file path

    remove_unrelated_rows(input_file, output_file)
