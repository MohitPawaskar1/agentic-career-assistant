import pandas as pd


def load_portfolio(file_path):
    df = pd.read_csv(file_path)

    docs = []
    for _, row in df.iterrows():
        docs.append({
            "text": f"{row['Techstack']} {row['Description']}",
            "link": row["Links"]
        })

    return docs


def load_resume(file_path):
    with open(file_path, "r") as f:
        return f.read()