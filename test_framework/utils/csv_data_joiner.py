import pandas as pd
import os


def read_test_data(testcase_id):
    # Get project root (one level up from current file)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Build full path dynamically
    file_path = os.path.join(base_dir, "testdata", "web", "login.csv")

    df = pd.read_csv(file_path)

    filtered_df = df[df["testcaseid"] == testcase_id]

    if filtered_df.empty:
        raise ValueError(f"Test data not found for testcase_id: {testcase_id}")

    return filtered_df.iloc[0].to_dict()
