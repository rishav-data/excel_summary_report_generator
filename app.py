from flask import Flask, render_template, request, send_file, redirect
import os
from werkzeug.utils import secure_filename
from file_loader import load_data, list_excel_sheets
from analyzer import summarize_data
from visualizer import generate_charts
from pdf_generator import create_pdf
import pandas as pd
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = "sample_files"
OUTPUT_FOLDER = "output_reports"
CHART_FOLDER = os.path.join(OUTPUT_FOLDER, "charts")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return "No file selected."

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file.save(file_path)

        if file_path.endswith(('.xls', '.xlsx')):
            sheets = list_excel_sheets(file_path)
            return render_template('select_sheet.html', file=filename, sheets=sheets)

        return redirect(f'/generate?file={filename}&sheet=')

    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate_report():
    filename = request.args.get('file')
    sheet = request.args.get('sheet', default=0)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    try:
        sheet_name = int(sheet) if sheet.isdigit() else sheet
        df = load_data(file_path, sheet_name=sheet_name)
    except Exception as e:
        return f"Error loading data: {e}"

    if df.empty:
        return "Uploaded file contains no usable data."

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    os.makedirs(CHART_FOLDER, exist_ok=True)

    summary_df = summarize_data(df)
    chart_paths = generate_charts(df, CHART_FOLDER)

    report_name = f"report_{uuid.uuid4().hex[:8]}.pdf"
    report_path = os.path.join(OUTPUT_FOLDER, report_name)
    create_pdf(summary_df, chart_paths, report_path)

    return send_file(report_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
