from fpdf import FPDF
import pandas as pd

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Auto-Generated Report", ln=True, align="C")

    def add_summary(self, summary_df):
        self.set_font("Arial", size=10)
        self.ln(10)
        for col, row in summary_df.iterrows():
            self.set_font("Arial", "B", 12)
            self.cell(0, 8, f"Column: {col}", ln=True)
            self.set_font("Arial", size=10)
            for stat, value in row.items():
                if pd.notna(value):
                    if isinstance(value, float):
                        value = round(value, 2)
                    self.cell(0, 8, f"- {stat.capitalize():<8}: {value}", ln=True)
            self.ln(4)

    def add_charts(self, chart_paths):
        for chart in chart_paths:
            self.add_page()
            self.image(chart, x=10, w=180)

def create_pdf(summary_df, chart_paths, output_path):
    pdf = PDFReport()
    pdf.add_page()
    pdf.add_summary(summary_df)
    pdf.add_charts(chart_paths)
    pdf.output(output_path)
