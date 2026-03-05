# CSV Cleaner

CSV Cleaner is a simple Python automation tool designed to clean and organize CSV datasets automatically.

This project was created to help businesses and analysts process messy CSV files quickly by removing duplicates, standardizing data, and preparing the dataset for Excel analysis.

---

# Features

- Remove duplicate rows automatically
- Clean inconsistent or messy data
- Reorganize dataset columns
- Export cleaned data to a structured Excel file
- Fast processing for large CSV files

---

# Example Use Case

Businesses often receive raw CSV files exported from different systems.  
These files usually contain duplicate entries, inconsistent formatting, or disorganized columns.

CSV Cleaner processes the dataset automatically and produces a clean and structured output ready for Excel or further analysis.

---

# Technologies Used

- Python
- pandas
- CSV processing
- Excel automation

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Ohlipeh/CSVCleaner.git
cd CSVCleaner
```

Create a virtual environment (recommended):

python -m venv .venv

Activate the environment:

Windows

.venv\Scripts\activate

Mac / Linux

source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt
How to Run

Run the script with:

python main.py

The script will process the CSV dataset and generate a cleaned output file ready for analysis.

Project Structure
CSVCleaner
│
├── main.py
├── requirements.txt
├── sample_data.csv
├── cleaned_data.xlsx
└── README.md
Example Workflow

Raw CSV File
⬇
CSV Cleaner Script
⬇
Cleaned Dataset
⬇
Excel-ready file for analysis

Screenshots

You can add example screenshots here showing:

Raw CSV dataset

Script running in terminal

Cleaned Excel output

Example:

assets/raw_data.png
assets/script_running.png
assets/cleaned_output.png
Author

Andre Felipe

GitHub:
https://github.com/Ohlipeh

License

This project is open source and available under the MIT License.
