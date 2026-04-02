import chromadb
import pandas as pd
import uuid


class ChromaStore:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="db")
        self.collection = self.client.get_or_create_collection(name="portfolio")

    def add_documents_from_csv(self, file_path):
        # load CSV
        df = pd.read_csv(file_path)

        # avoid duplicate inserts
        if self.collection.count() > 0:
            print("Data already exists. Skipping insert.")
            return

        # your same loop (unchanged logic)
        for index, row in df.iterrows():
            self.collection.add(
                documents=[f"{row['Techstack']} {row['Description']}"],
                metadatas=[
                    {
                        "description": row["Description"],
                        "links": row["Links"]
                    }
                ],
                ids=[str(uuid.uuid4())]
            )

        print("Data Added")

    def query(self, query_text, n_results=2):
        result = self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return result