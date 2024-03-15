import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_visualization(correlation_matrix):
    # Plot correlation matrix
    plt.imshow(correlation_matrix, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.title('Correlation Matrix')
    plt.xticks(np.arange(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
    plt.yticks(np.arange(len(correlation_matrix.index)), correlation_matrix.index)
    plt.tight_layout()
    plt.savefig('vis.png')
    plt.show()

if __name__ == "__main__":
    # Load correlation matrix from the dataset
    data = {
        'Pclass': [1.000000, -0.131900, -0.369226, -0.549500],
        'Sex': [-0.131900, 1.000000, -0.093254, 0.182333],
        'Age': [-0.369226, -0.093254, 1.000000, 0.096067],
        'Fare': [-0.549500, 0.182333, 0.096067, 1.000000]
    }
    correlation_matrix = pd.DataFrame(data)

    # Create visualization
    create_visualization(correlation_matrix)