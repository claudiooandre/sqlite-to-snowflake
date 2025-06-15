def clean_data(df):
    df = df.dropna()
    df['valor_total'] = df['quantidade'] * df['preco_uni']
    return df
