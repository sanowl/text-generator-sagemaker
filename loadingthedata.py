import pandas as pd

# Path to where you've saved the downloaded dataset
input_file_path = 'dataset/finefoods.txt'

# Assuming the file is tab-separated, change sep='\t' if it's different
try:
    # Use 'on_bad_lines' to handle any problematic lines
    df = pd.read_csv(input_file_path, sep='\t', on_bad_lines='skip')
except Exception as e:
    print(f"Error loading the dataset: {e}")
    exit()

# Optionally, perform any necessary preprocessing steps here

# Path where you want to save the new CSV file, changing the extension to .csv
output_file_path = 'dataset/finefoods_processed.csv'

# Save the DataFrame to a new CSV file
try:
    df.to_csv(output_file_path, index=False)
    print(f"Dataset saved to {output_file_path}")
except Exception as e:
    print(f"Error saving the dataset: {e}")