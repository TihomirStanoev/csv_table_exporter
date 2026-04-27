# 📊 CSV Table Exporter

A Python tool that reads production machine CSV exports, processes the data, and outputs a formatted Excel file.

## ✨ What it does

- Loads multiple CSV files from a folder
- Filters and deduplicates records
- Calculates good, bad and total quantities per shift and date
- Exports a structured Excel file with a named range

## 🚀 Getting started

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Configure:**
```bash
cp config.example.py config.py
```
Edit `config.py` with your own values.

**Run:**
```bash
python main.py
```

Place your CSV files in the `exports/` folder before running.

## 📁 Project structure

```
csv_table_exporter/
├── main.py
├── config.example.py       # template — copy to config.py
├── data_transform/
│   ├── variables.py
│   ├── csv_loader.py
│   ├── decorators.py
│   └── processors/
│       ├── lnr_processor.py
│       └── table_processor.py
└── requirements.txt
```

## 🔧 Requirements

- Python 3.12+
- pandas, openpyxl, numpy
