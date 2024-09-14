import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filename):
    return pd.read_csv(filename)

def visualize_data(df):
    plt.figure(figsize=(10, 6))
    
    # Example: Bar plot of keywords frequency
    keywords = ['innovative', 'leading', 'customer-focused']
    counts = [df['Description'].str.contains(keyword, case=False).sum() for keyword in keywords]
    sns.barplot(x=keywords, y=counts)
    plt.xlabel('Keywords')
    plt.ylabel('Frequency')
    plt.title('Frequency of Keywords in Competitor Descriptions')
    plt.show()

if __name__ == "__main__":
    df = load_data('competitors.csv')
    visualize_data(df)