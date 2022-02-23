import pandas as pd
import pathpy as pp

def load_df():
    network_df = pd.read_excel (r'manufacturing_emails_temporal_network.xlsx')
    return network_df

def load_df_as_network(df):
    temporal = pp.TemporalNetwork()
    for ind in df.index:
        temporal.add_edge(df['node1'][ind], df['node2'][ind], int(df['timestamp'][ind]))
    print(temporal)


if __name__ == "__main__":
    net_df = load_df()
    load_df_as_network(net_df)
