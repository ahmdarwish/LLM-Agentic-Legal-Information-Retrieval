# LLM Agentic Legal Information Retrieval

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Kaggle Competition](https://img.shields.io/badge/Kaggle-Competition-20beff.svg)](https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0)

This repository contains the foundational code and baselines for the **[LLM Agentic Legal Information Retrieval](https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview)** Kaggle competition. 

The challenge focuses on building an LLM-powered agentic retrieval pipeline for Swiss law. Given a legal question in English, the system must accurately retrieve the most relevant Swiss legal sources (statutes, decisions, etc., which are mostly cited in German). Submissions are evaluated on a hidden test set using citation-level Macro F1.

## 🚀 Quick Start

### Installation

bash
import kagglehub
kagglehub.login()
path = kagglehub.competition_download('llm-agentic-legal-information-retrieval')

### Download Data
 Get it from Kaggle 

 ### Run Baselines
 One baseline is created (https://github.com/ahmdarwish/LLM-Agentic-Legal-Information-Retrieval/blob/main/code_baseline.ipynb)

 ## Data Format
Training set: LEXam (Fan et al., 2025) open-question queries with gold citations extracted from "answer" field.
Source: https://huggingface.co/datasets/LEXam-Benchmark/LEXam/viewer/open_question
Paper: https://arxiv.org/abs/2505.12864
License: Creative Commons Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/
No endorsement: The LEXam authors and Hugging Face do not endorse or sponsor this competition.
Test set: queries only; final ranking is based on a hidden set of similar queries. The process used for creating this data is confidential, please do not publicly speculate about it.
Retrieval corpus: Swiss federal laws and federal court decision considerations (the searchable sources)
Under Swiss law, official enactments and official decisions/reports of authorities are not protected by copyright (Swiss Copyright Act, Art. 5). The excerpts are provided for research/competition purposes; no guarantee of completeness or official status.

## Project Structure
bash
├── src/omnilex/           # Core library
│   ├── citations/         # Citation parsing & regex normalization
│   ├── evaluation/        # Metrics (Macro F1) & scoring
│   ├── retrieval/         # Dense vector search & BM25 tools
│   └── llm/               # Local LLM loading & prompt engineering
├── notebooks/             # Baseline architectures (Search vs. Generation)
├── scripts/               # Utility scripts (e.g., validate_submission.py)
├── tests/                 # Test suite
└── data/                  # Data directory (ignored in git)

## Requirement
Python >= 3.10
llama-cpp-python (for local LLM inference)
rank-bm25 (for keyword search)
pandas, numpy, scikit-learn

## Contact
For public questions about the competition please open an issue on this repository.
