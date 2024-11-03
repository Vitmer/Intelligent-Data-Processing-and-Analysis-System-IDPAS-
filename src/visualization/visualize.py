import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

def plot_confusion_matrix(y_true, y_pred):
    """Plot a confusion matrix."""
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()

def plot_feature_importances(model, feature_names):
    """Plot feature importances."""
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]

    plt.figure(figsize=(10, 6))
    plt.title('Feature Importances')
    plt.bar(range(len(importances)), importances[indices], align='center')
    plt.xticks(range(len(importances)), [feature_names[i] for i in indices], rotation=90)
    plt.xlim([-1, len(importances)])
    plt.show()

if __name__ == "__main__":
    # Load the dataset
    data = pd.read_csv("data/iris.csv", header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])
    target_column = 'class'

    # Prepare data
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    # Train the model
    model = RandomForestClassifier()
    model.fit(X, y)
    
    # Make predictions
    y_pred = model.predict(X)

    # Plot the confusion matrix
    plot_confusion_matrix(y, y_pred)

    # Plot feature importances
    plot_feature_importances(model, X.columns)