import argparse
import pandas as pd
import subprocess

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except Exception as e:
        print("Error:", e)
        return None

def main():
    parser = argparse.ArgumentParser(description="Load dataset from a file and transfer to dpre.py")
    parser.add_argument("file_path", type=str, help="Path to the dataset file")
    args = parser.parse_args()

    dataset = load_dataset(args.file_path)
    if dataset is not None:
        print("Dataset loaded successfully:")
        print(dataset.head())

        try:
            # Specify the use of python3 explicitly
            subprocess.run(["python3", "dpre.py", args.file_path])
            print("Dataset transferred to dpre.py successfully.")
        except Exception as e:
            print("Error while transferring dataset to dpre.py:", e)

if __name__ == "__main__":
    main()