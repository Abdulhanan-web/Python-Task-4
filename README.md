# 📊 System Log Analyzer (Python CLI Tool)

A powerful yet simple **command-line log analyzer** built using Python. This tool allows users to load system log files, analyze their contents, search for specific entries, filter logs, and generate reports in multiple formats.

---

## 🚀 Features

* 📂 Load and parse log files
* 📊 Analyze log statistics (Error, Warning, Info counts)
* 🔍 Search logs by keyword
* 📁 Filter logs by log level and date
* 📝 Generate reports (TXT & CSV formats)
* 🖥️ Interactive command-line interface

---

## 🛠️ Technologies Used

* **Python 3**
* Built-in Libraries:

  * `re` – Regular Expressions for log parsing
  * `os` – File handling
  * `csv` – Report generation
  * `datetime` – Date handling

---

## 📁 Project Structure

```
project-folder/
│
├── log_analyzer.py   # Main Python script
└── README.md         # Project documentation
```

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed:

```bash
python --version
```

### Step 2: Run the Program

```bash
python log_analyzer.py
```

---

## 📌 Usage Guide

### 🔹 1. Load Log File

* Enter the full file path when prompted.
* The system extracts:

  * Timestamp
  * Log Level (ERROR, WARNING, INFO)
  * Message

---

### 🔹 2. Analyze Logs

Displays:

* Total number of logs
* Number of Errors
* Number of Warnings
* Number of Info messages

---

### 🔹 3. Search Logs

* Enter a keyword
* Displays all matching log entries

---

### 🔹 4. Filter Logs

Filter logs using:

* Log level (ERROR / WARNING / INFO)
* Date (format: `YYYY-MM-DD`)

---

### 🔹 5. Generate Report

* Generates a summary report
* Option to save:

  * 📄 TXT file (`report.txt`)
  * 📊 CSV file (`report.csv`)

---

## 📄 Supported Log Format

The program uses regex to parse logs. Example format:

```
2025-05-05 12:30:45 ERROR Something went wrong
2025-05-05 12:31:00 INFO System started
2025-05-05 12:32:10 WARNING Low memory
```

---

## ⚠️ Limitations

* Only supports logs containing:

  * `ERROR`, `WARNING`, `INFO`
* Timestamp format must be:

  ```
  YYYY-MM-DD HH:MM:SS
  ```
* May not work correctly with complex or custom log formats without modifying regex

---

## 🔧 Future Improvements

* GUI version (Tkinter or Web-based UI)
* Support for additional log levels (DEBUG, CRITICAL)
* Export filtered logs
* Data visualization (charts & graphs)
* Real-time log monitoring

---

## 👨‍💻 Author

Developed as a learning project for:

* File handling
* Regular expressions
* CLI-based application development in Python

---

## 📜 License

This project is open-source and free to use for educational and personal purposes.

---

## ⭐ Contributing

Feel free to fork this repository and improve the project. Contributions are welcome!

---

## 💡 Tip

For best results, use well-structured log files that follow standard logging formats.

---
