# Agentic Deep-Research Pipeline: Modular Ablation Study

This repository contains an autonomous research agent system built to ingest, process, index, and verify complex research literature from the agentic computing domain. 

The core system combines a dual-index hybrid search core (using keyword BM25 alongside dense vector similarity), structural text planning loops, and an automated verification shield to eliminate hallucinated sources. To measure the value of each part, an evaluation script runs across 7 independent ablation setups against a 30-question test bank.

---

## 📁 Repository Structure

* **data/**
  * **raw_pdfs/** : PDF documents collected directly from arXiv.
  * **processed_txt/** : Cleaned, paragraph-by-paragraph text segments.
* **eval/**
  * **questions.jsonl** : The provided 30-question benchmark dataset.
* **predictions/** : Evaluation outputs containing 1 line of JSON per question.
  * `full_agent.jsonl` : Complete, unbroken pipeline track.
  * `baseline.jsonl` : Standard lookup baseline.
  * `no_hybrid.jsonl` : Ablation track using dense search only.
  * `no_planner.jsonl` : Ablation track with planning layers turned off.
  * `no_reflector.jsonl` : Ablation track with reflective modules turned off.
  * `no_reranker.jsonl` : Ablation track with the paragraph reranker turned off.
  * `no_verifier.jsonl` : Ablation track with the fact-checking gate turned off.
* **.gitignore** : Excludes local caching files, bytecodes, and the venv folder.
* **ingest.py** : Automated downloading, parsing, and cleaning pipeline.
* **main.py** : Main engine managing the retrieval loops and multi-track evaluation.
* **requirements.txt** : Declared production package versions.
* **Technical Report - DTU.pdf** : Final academic submission document.

---

## 🛠️ Installation and Setup

Follow these exact steps from a fresh repository clone to build your environment:

### 1. Set Up a Virtual Environment
Open your standard terminal or PowerShell screen in the project's root folder and execute:
```powershell
python -m venv venv
.\venv\Scripts\activate

---

## 2. Install Project Requirements
Install the locked framework dependencies from the local tracker file:

pip install -r requirements.txt
