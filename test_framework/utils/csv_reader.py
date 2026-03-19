import csv
import os


# ─────────────────────────────────────────
# Base function - reads any CSV file
# ─────────────────────────────────────────
def read_csv(file_path):
    """Base function - reads any CSV file"""
    records = []
    # If the given path doesn't exist as-is, try resolving it
    # relative to the project `testdata` directory (sibling of utils).
    resolved_path = file_path
    if not os.path.exists(resolved_path):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        alt_path = os.path.join(base_dir, file_path)
        if os.path.exists(alt_path):
            resolved_path = alt_path
        else:
            raise FileNotFoundError(f"CSV file not found: {file_path}")

    with open(resolved_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    return records


# ─────────────────────────────────────────
# Mobile functions
# ─────────────────────────────────────────
def get_test_data(filename):
    """
    Reads CSV file and returns list of tuples
    (contact_name, message)
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "testdata", "mobile", filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    test_data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            contact_name = row['contact_name']
            message = row['message']
            test_data.append((contact_name, message))

    print(f"✅ Loaded {len(test_data)} rows from {filename}")
    return test_data


def get_status_data(filename):
    """
    Reads whatsappstatus_data.csv
    and returns list of status names
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "testdata", "mobile", filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    status_data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            status_name = row['status_name']
            status_data.append(status_name)

    print(f"✅ Loaded {len(status_data)} status names from {filename}")
    return status_data


# ─────────────────────────────────────────
# Web functions
# ─────────────────────────────────────────
def get_web_data(filename):
    """
    Reads web CSV files
    Returns list of dictionaries
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "testdata", "web", filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    records = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append(row)

    print(f"✅ Loaded {len(records)} rows from {filename}")
    return records


# ─────────────────────────────────────────
# API functions
# ─────────────────────────────────────────
def get_api_data(filename):
    """
    Reads api CSV files
    Returns list of dictionaries
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "testdata", "api", filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    records = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append(row)

    print(f"✅ Loaded {len(records)} rows from {filename}")
    return records
