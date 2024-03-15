import subprocess
import pandas as pd
import numpy as np

def exploratory_data_analysis(df):
    insights = []

    # Identify non-numeric columns
    non_numeric_columns = df.select_dtypes(exclude=['float64', 'int64']).columns

    # Remove non-numeric columns or convert them to numeric values
    numeric_df = df.drop(columns=non_numeric_columns)

    # Insight 1: Summary Statistics
    summary_stats = numeric_df.describe()
    insight1 = "Insight 1: Summary Statistics\n" + str(summary_stats) + "\n"
    insights.append(insight1)

    # Insight 2: Correlation Analysis
    # Convert non-numeric values to NaN
    df_numeric = df.apply(pd.to_numeric, errors='coerce')
    correlation_matrix = df_numeric.corr()
    insight2 = "Insight 2: Correlation Matrix\n" + str(correlation_matrix) + "\n"
    insights.append(insight2)

    # Insight 3: Value Counts for Categorical Variables
    for col in non_numeric_columns:
        value_counts = df[col].value_counts()
        insight3 = f"Insight 3: Value Counts for {col}\n" + str(value_counts) + "\n"
        insights.append(insight3)

    return insights

def save_insights(insights):
    for i, insight in enumerate(insights, start=1):
        file_name = f"eda-in-{i}.txt"
        with open(file_name, "w") as file:
            file.write(insight)

def main():
    # Load preprocessed dataset from CSV
    try:
        df = pd.read_csv("res_dpre.csv")
    except FileNotFoundError:
        print("Error: Preprocessed dataset file 'res_dpre.csv' not found.")
        return

    # Perform exploratory data analysis
    insights = exploratory_data_analysis(df)

    # Save insights as text files
    save_insights(insights)

if __name__ == "__main__":
    main()