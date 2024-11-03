import pandas as pd

def clean_data(data):
    """Clean the data: remove missing values and duplicates."""
    if data is not None:
        # Remove missing values
        data.dropna(inplace=True)
        # Remove duplicates
        data.drop_duplicates(inplace=True)
        print("Data cleaned.")
        return data
    else:
        print("No data to clean.")
        return None

if __name__ == "__main__":
    # Load the dataset
    data = pd.read_csv("data/iris.csv", header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

    # Clean the data
    cleaned_data = clean_data(data)

    if cleaned_data is not None:
        print(cleaned_data.head())  # Print the first 5 rows of the cleaned data