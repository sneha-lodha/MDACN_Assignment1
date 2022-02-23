import pandas as pd

def load_df():
    df = pd.read_excel (r'manufacturing_emails_temporal_network.xlsx')
    print (df)

if __name__ == "__main__":
    load_df()