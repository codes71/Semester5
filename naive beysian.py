# Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Load the Titanic dataset
def load_titanic_data():
    url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    df = pd.read_csv(url)
    return df

# Data preprocessing
def preprocess_data(df):
    # Select relevant features
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
    X = df[features].copy()
    y = df['Survived']
    
    # Handle missing values
    X['Age'].fillna(X['Age'].mean(), inplace=True)
    X['Fare'].fillna(X['Fare'].mean(), inplace=True)
    
    # Convert categorical variables
    le = LabelEncoder()
    X['Sex'] = le.fit_transform(X['Sex'])
    
    return X, y

# Main execution
def main():
    # Load data
    df = load_titanic_data()
    
    # Preprocess data
    X, y = preprocess_data(df)
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the Naive Bayes classifier
    nb_classifier = GaussianNB()
    nb_classifier.fit(X_train, y_train)
    
    # Make predictions
    y_pred = nb_classifier.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Print results
    print("Naive Bayes Classifier Results:")
    print("--------------------------------")
    print(f"Accuracy: {accuracy:.2f}")
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()