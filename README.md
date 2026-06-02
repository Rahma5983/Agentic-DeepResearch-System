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
2. Install Project RequirementsInstall the locked framework dependencies from the local tracker file:PowerShellpip install -r requirements.txt
⚙️ Reproducing Results (Single Command)To rebuild the corpus matrices, run all 30 test questions across every individual testing state, and regenerate the tables listed in the research paper, run the single command:PowerShellpython main.py
Process Timeline:main.py maps the extracted text datasets located in data/processed_txt/.It spins up a keyword locator alongside a dense vector layout using a local all-MiniLM-L6-v2 script running entirely on your machine's CPU.The engine parses the queries inside eval/questions.jsonl while maintaining hard text size bounds (factoid, comparative, or survey layouts).The script saves 7 separate prediction tracks straight into the predictions/ folder.📊 Summary of Empirical ResultsSystem Configuration / VariantRow CountCitation F1-ScoreLength Rule ComplianceFake Citations Blockedfull_agent30 / 3098.2%100%0 (Perfect)baseline30 / 3064.1%100%0no_planner30 / 3085.5%100%0no_hybrid30 / 3071.0%100%0no_reranker30 / 3089.1%100%0no_reflector30 / 3082.4%100%0no_verifier30 / 3041.3%100%+30 Injected📝 Submission Format ComplianceEvery line inside your generated output files prints out matching the exact submission criteria required by the grader:JSON{"id": "q01", "answer": "The Agent-Computer Interface handles context scaling...", "cited_papers": ["2405.15793"]}
id : Maps precisely to the question identifier token.answer : Clear text response bounded strictly by lengths rules.cited_papers : A simple flat array list holding the clean arXiv strings.
