def summarize_data(df):
    summary = df.describe(include='all').transpose()
    return summary