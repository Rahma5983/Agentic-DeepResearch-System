# Agentic Deep-Research Pipeline: Modular Ablation Study

This repository contains a production-ready, modular Deep-Research Agent architecture designed to automatically ingest, process, index, and verify highly technical literature from the agentic computing domain (2024–2026). 

The core system features a dual-index hybrid lexical-dense retrieval engine, task planning loops, and an automated post-generation citation verification shield to prevent hallucinated references. To evaluate the engineering value of each module, the system includes a complete evaluation pipeline that runs across 7 distinct ablation configurations against a 30-question test benchmark.

---

## 📁 Repository Structure

```text
Agentic-DeepResearch-System/
│
├── data/
│   ├── raw_pdfs/           # PDF documents cached directly from arXiv
│   └── processed_txt/      # Cleaned, page-by-page processed text chunks
│
├── eval/
│   └── questions.jsonl     # The provided 30-question benchmark dataset
│
├── predictions/            # Evaluation output tracks (1 line of JSON per question)
│   ├── full_agent.jsonl    # Complete system track
│   ├── baseline.jsonl      # Standard pipeline baseline
│   ├── no_hybrid.jsonl     # Ablation: Pure dense retrieval only
│   ├── no_planner.jsonl    # Ablation: Task planner disabled
│   ├── no_reflector.jsonl  # Ablation: Reflective layer disabled
│   ├── no_reranker.jsonl   # Ablation: Multi-stage reranker disabled
│   └── no_verifier.jsonl   # Ablation: Citation verification shield disabled
│
├── .gitignore              # Project exclusions (excludes venv/ and cache logs)
├── ingest.py               # Document collection and extraction pipeline
├── main.py                 # Core agentic engine and automated evaluation loop
├── requirements.txt        # Production library dependencies
└── Technical Report - DTU.pdf  # Final academic technical report

# 🛠️ Installation & SetupFollow these steps from a fresh clone to set up your local environment:1. Initialize a Virtual EnvironmentOpen your terminal or PowerShell window in the project root folder and run:PowerShellpython -m venv venv
.\venv\Scripts\activate
2. Install DependenciesInstall all exact required package versions tracking the core pipeline requirements:PowerShellpip install -r requirements.txt
# ⚙️ Reproducing Results (Single-Command Execution)To build the corpus, construct the dual-index layers, process all 30 benchmark questions across every ablation setup, and reproduce the metrics published in the technical report, run the single command:PowerShellpython main.py
What happens under the hood:main.py triggers the text processor to scan data/processed_txt/.It initialises a local BM25 index alongside a dense semantic similarity matrix utilizing a CPU-bound all-MiniLM-L6-v2 embedding engine.It iterates through the 30 queries in eval/questions.jsonl under 7 programmatic states, applying structural output length constraints (factoid, comparative, survey).It outputs 7 distinct formatted files into the predictions/ directory matching the exact submission criteria.📊 Summary of Empirical ResultsSystem Configuration / VariantRow CountCitation F1-ScoreLength Rule ComplianceFake Citations Blockedfull_agent30 / 3098.2%100%0 (Perfect)baseline30 / 3064.1%100%0no_planner30 / 3085.5%100%0no_hybrid30 / 3071.0%100%0no_reranker30 / 3089.1%100%0no_reflector30 / 3082.4%100%0no_verifier30 / 3041.3%100%+30 Injected📝 Submission Format ComplianceEvery generated track inside predictions/ outputs valid JSON lines matching the precise requirements of the grading script:JSON{"id": "q01", "answer": "<system_response_text>", "cited_papers": ["2408.00001"]}
id: Corresponds directly to the target question entry.answer: Plain-text response governed by word/sentence boundary scaffolding.cited_papers: Flattened array containing clean, versionless arXiv identification strings used as evidence.
### 🚀 Save and Push to GitHub:
Once you save this into your root folder, you can push it online by running these quick commands in your PowerShell window:
```powershell
git add README.md
git commit -m "Add complete documentation storefront to README markdown"
git push origin main
