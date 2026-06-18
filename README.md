# LLM Agentic Legal Information Retrieval

This repository contains the code, notebooks, and sample data for our submission to the **LLM Agentic Legal Information Retrieval** Kaggle competition.

---

## **Project Overview**

The goal of this competition is to retrieve **Swiss legal citations** from English legal queries.  
Our final system combines:

- BM25 lexical retrieval over a Swiss legal corpus
- English → German dictionary expansion
- Qwen 3 0.6B LLM query expansion (for search terms)
- Direct citation extraction from the query
- Train-query support (optional, from similar training queries)
- Citation prior weighting and law-code boosting
- Noise filtering and final ranking

The pipeline returns the **top N citations** per query, formatted for Kaggle submission.

**Final Results:**

- Public Score: **0.03038**
- Private Score: **0.07587**

---

## **Repository Structure**
llm-agentic-legal-information-retrieval/
├─ notebooks/
│ └─ llmtest3.ipynb # Final notebook
├─ scripts/ # Optional: reusable functions
│ ├─ bm25_utils.py # BM25 class and tokenizer
│ ├─ query_expansion.py # Dictionary and query expansion functions
│ ├─ scoring.py # Citation parsing and F1 scoring
│ └─ direct_citation.py # Direct citation extraction functions
├─ data/ # Small sample datasets for reproducibility
│ ├─ train_sample.csv
│ ├─ test_sample.csv
│ ├─ laws_sample.csv
│ └─ sample_submission.csv
├─ submission/
│ └─ submission.csv # Final Kaggle submission
├─ requirements.txt # Python dependencies
└─ README.md


Notes on Full Dataset
The full dataset is too large to host on GitHub.
To run the full pipeline with complete data, download the datasets from the Kaggle competition page:

[LLM Agentic Legal Information Retrieval Data
](https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval)

Replace the sample CSV files in data/ with the full dataset files, keeping the same filenames if desired.


Pipeline Explanation
1. Direct Citation Extraction: Prioritize citations already mentioned in the query.
2. Query Expansion: Convert English terms to German legal terms via dictionary and Qwen 3 0.6B LLM.
3. BM25 Retrieval: Rank candidate legal documents.
4. Law-code Boosting & Citation Prior: Increase scores of likely law codes and frequent citations.
5. Noise Filtering: Remove repeated or irrelevant citations.
6. Final Ranking: Combine all signals to select top N citations per query.


Reproducibility
The notebook is fully runnable using the sample dataset in the data/ folder.
scripts/ contains all reusable functions.
submission/submission.csv shows the correct Kaggle format.
