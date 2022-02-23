import pandas as pd

def load_df():
    df = pd.read_excel (r'manufacturing_emails_temporal_network.xlsx')
    res = pd.concat([df["node1"], df["node2"]]).unique()
    print (pd.concat([df["node1"], df["node2"]]))

if __name__ == "__main__":
    load_df()