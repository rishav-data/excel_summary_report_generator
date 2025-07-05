import pandas as pd

def list_excel_sheets(file_path):
    """Returns a list of sheet names from an Excel file."""
    try:
        return pd.ExcelFile(file_path).sheet_names
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {e}")

def load_data(file_path, sheet_name=0):
    """Loads data from a CSV, Excel, or JSON file."""
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file_path, sheet_name=sheet_name)
        elif file_path.endswith('.json'):
            df = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format. Use CSV, Excel, or JSON.")
        
        return clean_data(df)

    except Exception as e:
        raise ValueError(f"Failed to load file: {e}")

def clean_data(df):
    """Cleans the DataFrame by removing empty rows and columns."""
    df = df.dropna(how='all')  # Remove fully empty rows
    df = df.dropna(axis=1, how='all')  # Remove fully empty columns
    df.columns = df.columns.astype(str)  # Ensure column headers are strings
    return df
