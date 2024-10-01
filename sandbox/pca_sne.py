
from portfolio_management.data.data_loader import DataLoader
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # List of stock tickers to include in the portfolio
    tickers = ['MSFT', 'NVDA',]

    # Date range for historical data
    start_date = '2020-01-01'
    end_date = '2024-09-30'

    # Load data
    data_loader = DataLoader()
    stock_data = data_loader.load_data(tickers, start_date, end_date)
    print(stock_data.head())

    # Apply PCA
    pca = PCA(n_components=2)
    stock_pca = pca.fit_transform(stock_data)

    # Visualize PCA output
    plt.scatter(stock_pca[:, 0], stock_pca[:, 1])
    plt.xlabel('PC 1')
    plt.ylabel('PC 2')
    plt.title('PCA Output')
    plt.show()

    tsne = TSNE(n_components=2)
    stock_tsne = tsne.fit_transform(stock_data)

    # Visualize t-SNE output
    plt.scatter(stock_tsne[:, 0], stock_tsne[:, 1], c=iris.target)
    plt.xlabel('t-SNE 1')
    plt.ylabel('t-SNE 2')
    plt.title('t-SNE Output')
    plt.show()
