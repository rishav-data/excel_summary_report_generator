⚠️VISIT https://excel-report-generator.onrender.com/ TO VIEW THE APPLICATION DIRECTLY 
OR 
⚠️OPEN THE report_generator FOLDER AND NAVIGATE TO run_report_generator.bash . OPEN THE BASH FILE AND WAIT FOR THE TERMINAL TO START THE FLASK AT A LOCAL HOST . ONCE THE LINK IS GENERATED , PASTET THE LINK ON BROWSER AND VISIT IT TO USE THE APPLICATION 
---
# 📊 Report Generator Web App

This is a lightweight web application for generating automated PDF reports from Excel, CSV, or JSON files. Users can upload a file, view and select sheets (for Excel), and download a structured report that includes statistical summaries and data visualizations.

---

## 🚀 Features

- 📁 Upload `.xlsx`, `.xls`, `.csv`, or `.json` files
- 📄 Choose a sheet from Excel files (if applicable)
- 📊 Automatically summarizes data
- 📈 Generates charts:
  - Pairwise scatterplots
  - Histograms
  - Bar charts for categorical columns
- 📑 Combines charts + stats into a downloadable PDF report
- 💻 Simple and responsive web interface (HTML/CSS)

---

## 🧠 Technologies Used

| Task                | Library/Tool                  |
|---------------------|-------------------------------|
| Read data           | `pandas`                      |
| Handle Excel        | `openpyxl`, `xlrd`            |
| Handle JSON/CSV     | `pandas` (built-in)           |
| Plot graphs         | `matplotlib`, `seaborn`       |
| Save charts         | `matplotlib.pyplot.savefig()` |
| Generate PDF        | `FPDF`                        |
| Web Framework       | `Flask`                       |
| Optional GUI (later)| `Streamlit` / `Tkinter`       |

---
## 🌉 Structure

report_generator/
├── templates/
│   └── index.html             # Web UI
│   └── select_sheet.html               
├── app.py  
├── main.py                  # Main script: orchestrates the process
├── file_loader.py           # Reads Excel/CSV/JSON into DataFrame
├── analyzer.py              # Performs summarization/cleaning
├── visualizer.py            # Generates charts and saves images
├── pdf_generator.py         # Combines text + charts into PDF
├── sample_files/            # Test files (CSV, Excel, JSON)
├── output_reports/          # Generated PDF reports
├──run_report_generator.bash #Double click to deploy Flask app
└── requirements.txt         # Required Python packages
