import re
import os
import csv
from datetime import datetime

# =========================
# Global Variables
# =========================
log_data = []
log_file_path = None

# Regex patterns
LOG_PATTERN = re.compile(r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})?.*?(?P<level>ERROR|WARNING|INFO).*?(?P<message>.*)", re.IGNORECASE)

# =========================
# Load Log File
# =========================
def load_log_file():
    global log_data, log_file_path
    path = input("Enter log file path: ").strip()

    if not os.path.exists(path):
        print("❌ File not found!")
        return

    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if not lines:
            print("⚠️ File is empty!")
            return

        log_data = []
        for line in lines:
            match = LOG_PATTERN.search(line)
            if match:
                log_data.append({
                    "timestamp": match.group("timestamp"),
                    "level": match.group("level").upper(),
                    "message": match.group("message").strip()
                })

        log_file_path = path
        print(f"✅ Loaded {len(log_data)} log entries.")

    except Exception as e:
        print(f"❌ Error reading file: {e}")

# =========================
# Analyze Logs
# =========================
def analyze_logs():
    if not log_data:
        print("⚠️ No logs loaded!")
        return

    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}

    for log in log_data:
        if log['level'] in counts:
            counts[log['level']] += 1

    print("\n📊 Log Analysis:")
    print(f"Total Logs: {len(log_data)}")
    print(f"Errors: {counts['ERROR']}")
    print(f"Warnings: {counts['WARNING']}")
    print(f"Info: {counts['INFO']}")

    return counts

# =========================
# Search Logs
# =========================
def search_logs():
    if not log_data:
        print("⚠️ No logs loaded!")
        return

    keyword = input("Enter keyword to search: ").lower()

    results = [log for log in log_data if keyword in log['message'].lower()]

    print(f"\n🔍 Found {len(results)} results:")
    for log in results:
        print(log)

# =========================
# Filter Logs
# =========================
def filter_logs():
    if not log_data:
        print("⚠️ No logs loaded!")
        return

    level = input("Enter level (ERROR/WARNING/INFO or leave blank): ").upper()
    date = input("Enter date (YYYY-MM-DD or leave blank): ")

    filtered = log_data

    if level:
        filtered = [log for log in filtered if log['level'] == level]

    if date:
        filtered = [log for log in filtered if log['timestamp'] and log['timestamp'].startswith(date)]

    print(f"\n📂 Filtered {len(filtered)} logs:")
    for log in filtered:
        print(log)

# =========================
# Generate Report
# =========================
def generate_report():
    if not log_data:
        print("⚠️ No logs loaded!")
        return

    counts = analyze_logs()

    report = {
        "Total Logs": len(log_data),
        "Errors": counts['ERROR'],
        "Warnings": counts['WARNING'],
        "Info": counts['INFO']
    }

    print("\n📝 Report Generated:")
    for k, v in report.items():
        print(f"{k}: {v}")

    save = input("Save report? (y/n): ").lower()
    if save == 'y':
        format_choice = input("Save as (1) TXT or (2) CSV: ")

        if format_choice == '1':
            with open("report.txt", "w") as f:
                for k, v in report.items():
                    f.write(f"{k}: {v}\n")
            print("✅ Report saved as report.txt")

        elif format_choice == '2':
            with open("report.csv", "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Metric", "Value"])
                for k, v in report.items():
                    writer.writerow([k, v])
            print("✅ Report saved as report.csv")

# =========================
# Menu System
# =========================
def menu():
    while True:
        print("""
======== System Log Analyzer ========
1. Load Log File
2. Analyze Logs
3. Search Logs
4. Filter Logs
5. Generate Report
6. Exit
====================================
        """)

        choice = input("Enter your choice: ")

        if choice == '1':
            load_log_file()
        elif choice == '2':
            analyze_logs()
        elif choice == '3':
            search_logs()
        elif choice == '4':
            filter_logs()
        elif choice == '5':
            generate_report()
        elif choice == '6':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice!")

# =========================
# Run Program
# =========================
if __name__ == "__main__":
    menu()
