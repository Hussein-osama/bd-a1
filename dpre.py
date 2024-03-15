import subprocess
import argparse
import pandas as pd
import shutil

def data_cleaning(df):
    null_values = df.isnull().sum()
    print("Null values in the dataset:")
    print(null_values)

    # Task 1: Remove duplicate rows
    df = df.drop_duplicates()



    # Task 3: Convert categorical values to numerical values
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

    # Task 4: Remove the 'Cabin' column
    df = df.drop(columns=['Cabin'])

    return df
def data_transformation(df):
    # Task 1: Feature scaling - normalize 'Fare' column
    df['Fare'] = (df['Fare'] - df['Fare'].mean()) / df['Fare'].std()

    # Task 2: Feature engineering - create new feature 'FamilySize'
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

    return df
def data_reduction(df):
    # Task 1: Select specific features
    selected_features = ['Pclass', 'Sex', 'Age', 'Fare', 'Embarked']
    df = df[selected_features]

    # Task 2: Drop columns not included in the selected features list
    all_columns = df.columns
    columns_to_drop = [col for col in all_columns if col not in selected_features]
    df = df.drop(columns=columns_to_drop)

    return df


def data_discretization(df):
    # Task 1: Discretize the 'Age' column into three age groups: 'Child', 'Adult', and 'Elderly'
    bins = [0, 18, 65, float('inf')]
    labels = ['Child', 'Adult', 'Elderly']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

    # Task 2: Discretize the 'Fare' column into three fare categories: 'Low', 'Medium', and 'High'
    # Adjust the bins and labels according to your dataset and requirements
    fare_bins = [0, 50, 100, float('inf')]
    fare_labels = ['Low', 'Medium', 'High']
    df['FareCategory'] = pd.cut(df['Fare'], bins=fare_bins, labels=fare_labels, right=False)

    return df

def main():
    parser = argparse.ArgumentParser(description="Perform data preprocessing tasks")
    parser.add_argument("file_path", type=str, help="Path to the input dataset file")
    args = parser.parse_args()

    try:
        df = pd.read_csv(args.file_path)
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except Exception as e:
        print("Error:", e)
        return

    # Data preprocessing tasks
    df = data_cleaning(df)
    if df is None:
        print("Error occurred during data cleaning.")
        return

    df = data_transformation(df)
    if df is None:
        print("Error occurred during data transformation.")
        return

    df = data_reduction(df)
    if df is None:
        print("Error occurred during data reduction.")
        return

    df = data_discretization(df)
    if df is None:
        print("Error occurred during data discretization.")
        return

    # Save preprocessed dataframe to CSV
    try:
        df.to_csv("res_dpre.csv", index=False)
        print("Preprocessed data saved to res_dpre.csv")

        # Call eda.py to generate insights
        subprocess.run(["python3", "eda.py"])
        print("EDA completed.")
    except Exception as e:
        print("Error occurred:", e)
    try:
        df.to_csv("res_dpre.csv", index=False)
        print("Preprocessed data saved to res_dpre.csv")

        # Call model.py to perform k-means clustering
        subprocess.run(["python3", "model.py", "res_dpre.csv"])
        print("K-means clustering completed.")
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    main()