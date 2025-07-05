import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_charts(df, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    chart_paths = []

    numeric_cols = df.select_dtypes(include='number').columns
    categorical_cols = df.select_dtypes(include='object').columns

    # Pairwise scatter plots for numeric columns
    if len(numeric_cols) >= 2:
        pairplot = sns.pairplot(df[numeric_cols])
        chart_path = os.path.join(output_dir, "pairplot.png")
        pairplot.savefig(chart_path)
        plt.close()
        chart_paths.append(chart_path)

    # Histograms for individual numeric columns
    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        chart_path = os.path.join(output_dir, f"{col}_hist.png")
        plt.savefig(chart_path)
        plt.close()
        chart_paths.append(chart_path)

    # Bar plots for categorical columns
    for col in categorical_cols:
        plt.figure(figsize=(6, 4))
        sns.countplot(y=df[col])
        plt.title(f"Counts of {col}")
        chart_path = os.path.join(output_dir, f"{col}_bar.png")
        plt.savefig(chart_path)
        plt.close()
        chart_paths.append(chart_path)
    return chart_paths
    if len(numeric_cols) >= 2:
        sns.scatterplot(data=df, x=numeric_cols[0], y=numeric_cols[1])
        plt.title(f"{numeric_cols[0]} vs {numeric_cols[1]}")
    elif len(numeric_cols) == 1:
        sns.histplot(df[numeric_cols[0]], kde=True)
        plt.title(f"Distribution of {numeric_cols[0]}")
    else:
        plt.text(0.5, 0.5, "No numeric columns", ha='center')

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
