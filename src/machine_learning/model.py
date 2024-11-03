import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(data, target_column):
    """Train a Random Forest model."""
    # Split the data into features and target variable
    X = data.drop(columns=[target_column])
    y = data[target_column]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")

    return model

if __name__ == "__main__":
    # Load the dataset
    data = pd.read_csv("data/iris.csv", header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

    # Train the model
    trained_model = train_model(data, target_column='class')