from sklearn.cluster import KMeans
import pandas as pd

def apply_kmeans(df):
    # Select columns suitable for K-means
    kmeans_data = df[['Pclass', 'Fare']]

    # Apply K-means clustering with k=3
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(kmeans_data)

    # Count the number of records in each cluster
    cluster_counts = pd.Series(clusters).value_counts().sort_index()

    # Save the counts to a text file
    cluster_counts.to_csv('k.txt', header=False)

def main():
    # Load the preprocessed dataset from CSV
    try:
        df = pd.read_csv("res_dpre.csv")
    except FileNotFoundError:
        print("Error: Preprocessed dataset file 'res_dpre.csv' not found.")
        return

    # Apply K-means clustering
    apply_kmeans(df)

if __name__ == "__main__":
    main()