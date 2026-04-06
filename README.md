# ⚖️ Omnilex Agentic Retrieval Competition - Starter Repo

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Kaggle Competition](https://img.shields.io/badge/Kaggle-Competition-20beff.svg)](https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-yellow.svg)](https://opensource.org/licenses/Apache-2.0)

This repository contains the foundational code and baselines for the **[LLM Agentic Legal Information Retrieval](https://www.kaggle.com/competitions/llm-agentic-legal-information-retrieval/overview)** Kaggle competition. 

The challenge focuses on building an LLM-powered agentic retrieval pipeline for Swiss law. Given a legal question in English, the system must accurately retrieve the most relevant Swiss legal sources (statutes, decisions, etc., which are mostly cited in German). Submissions are evaluated on a hidden test set using citation-level Macro F1.

## 🚀 Quick Start

### 1. Installation

(Tested with Ubuntu-24.04 in WSL)

```bash
# Clone the repository
git clone [https://github.com/YourUsername/LLM-Agentic-Legal-Information-Retrieval.git](https://github.com/YourUsername/LLM-Agentic-Legal-Information-Retrieval.git)
cd LLM-Agentic-Legal-Information-Retrieval

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # for testing/linting

# Install package in development mode
pip install -e .
