import os
os.chdir(r"C:\Users\Rishav\OneDrive\Desktop\report generator\report_generator")
from file_loader import load_data, list_excel_sheets
from analyzer import summarize_data
from visualizer import generate_charts
print("Imported successfully!")
from pdf_generator import create_pdf
import pandas as pd

input_file = "sample_files/data.xlsx" 
print("Current Working Directory:", os.getcwd())
print("Looking for:", input_file)
print("File exists:", os.path.exists(input_file))

chart_file = "output_reports/chart.png"
report_file = "output_reports/final_report.pdf"

#Create output folder if not exists
os.makedirs("output_reports", exist_ok=True)

#Handle Excel sheets
sheet_name = 0
if input_file.endswith(('.xlsx', '.xls')):
    sheets = list_excel_sheets(input_file)
    print("Available Sheets:")
    for i, name in enumerate(sheets):
        print(f"{i}: {name}")
    
    try:
        sheet_index = int(input(f"Enter sheet number (0 to {len(sheets)-1}): "))
        sheet_name = sheets[sheet_index]
    except Exception as e:
        print("Invalid input. Defaulting to first sheet.")

# Load + Clean Data
df = load_data(input_file, sheet_name=sheet_name)

if df.empty:
    raise ValueError("The loaded file has no usable data!")

summary_df = summarize_data(df) 
chart_paths = generate_charts(df, "output_reports/charts")
create_pdf(summary_df, chart_paths, report_file)
print("Report generated at:", report_file)