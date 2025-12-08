⚠️VISIT https://excel-report-generator.onrender.com/ TO VIEW THE APPLICATION DIRECTLY 
OR 
⚠️OPEN THE report_generator FOLDER AND NAVIGATE TO run_report_generator.bash . OPEN THE BASH FILE AND WAIT FOR THE TERMINAL TO START THE FLASK AT A LOCAL HOST.
---
# 📊 Report Generator Web App

This is a lightweight web application for generating automated PDF reports from Excel, CSV, or JSON files. Users can upload a file, view and select sheets (for Excel), and download a structured report that includes statistical summaries and data visualizations.

---

<img width="1332" height="881" alt="ui1" src="https://github.com/user-attachments/assets/d3888a2d-64cf-445f-bcdb-744b3aaa8cf5" />

## 🚀 Features

- 📁 Upload `.xlsx`, `.xls`, `.csv`, or `.json` files
  <img width="1941" height="1097" alt="uploadpart" src="https://github.com/user-attachments/assets/abfeca80-2cd8-47e0-9138-e9a52ff54a83" />
- 📄 Choose a sheet from Excel files (if applicable)
  ......
  <img width="402" height="290" alt="exlsheet" src="https://github.com/user-attachments/assets/9d269967-ff57-4ce7-8be5-056eccdc2433" />
- 📊 Automatically summarizes data
  <img width="1582" height="737" alt="resuly1" src="https://github.com/user-attachments/assets/ce63ed32-e216-4326-a87d-6838dddfb114" />
  <img width="476" height="465" alt="result 2" src="https://github.com/user-attachments/assets/cc2e14e1-8741-4aef-ac16-3491251185f1" />
- 📈 Generates charts:
  <img width="1632" height="880" alt="graphdi" src="https://github.com/user-attachments/assets/88cec7fa-5368-4954-b40f-ba35d8c19ff2" />
  - Pairwise scatterplots 
  - Histograms
  - Bar charts for categorical columns
    <img width="1072" height="702" alt="graph 3" src="https://github.com/user-attachments/assets/441f1cfe-6eb1-4a69-a42d-7d74c4cf5b06" />
- 📑 Combines charts + stats into a downloadable PDF report
  <img width="1073" height="733" alt="graph2" src="https://github.com/user-attachments/assets/e94ed8a0-7f95-4184-92db-2825faf8fc42" />
  <img width="1061" height="692" alt="last graph jfieaudis" src="https://github.com/user-attachments/assets/cdc3f127-a21d-4e16-ab49-8013d4da3047" />

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
<img width="582" height="348" alt="Screenshot 2025-07-25 122224" src="https://github.com/user-attachments/assets/23f12dc3-35f7-4f60-8ca1-4f2234519362" />

