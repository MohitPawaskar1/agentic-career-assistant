# Agentic Career Assistant

This project is a foundational implementation of a Retrieval-Augmented Generation (RAG) system using ChromaDB. It stores and retrieves portfolio data to enable intelligent, context-aware applications such as resume optimization, skill gap detection, and personalized job outreach.

---

## Project Structure

```
agentic-career-assistant/
│
├── app/
│   ├── rag/
│   │   ├── chroma_store.py
│   │   ├── loader.py
│   │
│   ├── main.py
│
├── data/
│   ├── portfolio.csv
│   ├── resume.txt
│
├── db/                 # Local vector database (ignored in git)
├── .env
├── .gitignore
├── README.md
```

---

## How It Works

1. Portfolio data is loaded from a CSV file.
2. Data is converted into embeddings and stored in ChromaDB.
3. A query is passed to the system.
4. The system retrieves the most relevant portfolio entries.
5. Retrieved data can be used for downstream tasks such as resume optimization or email generation.

---

## Example Query

```
Looking for experience in Slurm HPC cluster management
```

---

## Tech Stack

- Python
- ChromaDB
- Sentence Transformers
- Pandas

---

## Installation

1. Clone the repository:

```
git clone https://github.com/MohitPawaskar1/agentic-career-assistant.git
cd agentic-career-assistant
```

2. Install dependencies using uv:

```
uv add chromadb pandas sentence-transformers
```

3. Run the application:

```
uv run python main.py
```

---

## Notes

- The vector database is stored locally in the `db/` directory.
- Ensure `.env` is not committed to version control.
- Data is inserted into the database only once using a persistent client.

---

## Future Improvements

- Resume analysis and skill gap detection  
- Automated resume optimization for specific job roles  
- Personalized email generation for job applications  
- Integration with LangGraph for multi-agent workflows  
- API or UI layer for user interaction  

---

## Author

Mohit Pawaskar