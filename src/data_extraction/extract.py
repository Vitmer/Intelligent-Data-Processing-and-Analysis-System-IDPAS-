import pandas as pd

def extract_data(file_path):
    """Extract data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Data successfully extracted from {file_path}")
        return data
    except Exception as e:
        print(f"Error while extracting data: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    data = extract_data("data/iris.csv")  # Update the path to your data file
    if data is not None:
        print(data.head())  # Print the first 5 rows of the data