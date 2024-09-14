import pandas as pd

def load_data(filename):
    return pd.read_csv(filename)

def analyze_competitors(df):
    # Basic statistics
    print("Total Competitors:", df[0])
    # Example: Frequency of certain keywords in descriptions
    keywords = ['innovative', 'leading', 'customer-focused']
    for keyword in keywords:
        count = df['Description'].str.contains(keyword, case=False).sum()
        print(f"Competitors mentioning '{keyword}':", count)

if __name__ == "__main__":
    df = load_data('competitors.csv')
    analyze_competitors(df)
