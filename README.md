# LLM Agentic Legal Information Retrieval

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Kaggle Competition](https://img.shields.io/badge/Kaggle-Competition-20beff.svg)](https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0)

This repository contains the foundational code and baselines for the **[LLM Agentic Legal Information Retrieval](https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview)** Kaggle competition. 

The challenge focuses on building an LLM-powered agentic retrieval pipeline for Swiss law. Given a legal question in English, the system must accurately retrieve the most relevant Swiss legal sources (statutes, decisions, etc., which are mostly cited in German). Submissions are evaluated on a hidden test set using citation-level Macro F1.

## 🚀 Quick Start

### Download Data
 Get it from Kaggle 

 ### Run Baselines
 One baseline is created (https://github.com/ahmdarwish/LLM-Agentic-Legal-Information-Retrieval/blob/main/code_baseline.ipynb)

 ## Data Format
The final system must predict a semicolon-separated list of exact citations for each query_id in the test set.

*Training Set: LEXam open-question queries with gold citations.

*Retrieval Corpus: Swiss federal laws and federal court decision considerations.

*Metric: Submissions are scored using Macro F1, computed per-query between your predicted citations and the gold citation set, and then averaged.

## Requirement
*Python >= 3.10
*llama-cpp-python (for local LLM inference)
*rank-bm25 (for keyword search)
*pandas, numpy, scikit-learn

## Contact
For public questions about the competition please open an issue on this repository.
