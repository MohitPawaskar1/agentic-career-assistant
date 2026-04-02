from app.rag.chroma_store import ChromaStore


def main():
    print("Program started")

    store = ChromaStore()

    # Load data only if DB is empty
    if store.collection.count() == 0:
        print("Loading data into DB...")
        store.add_documents_from_csv("data/portfolio.csv")
    else:
        print("DB already initialized")

    # Query
    query = "Looking for experience in Slurm HPC cluster management"
    result = store.query(query)

    documents = result["documents"]
    metadatas = result["metadatas"]

    print("\n--- Retrieved Documents ---")
    for doc in documents[0]:
        print("-", doc)

    print("\n--- Links ---")
    for meta in metadatas[0]:
        print("-", meta["links"])


if __name__ == "__main__":
    main()