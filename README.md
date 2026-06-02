<h1>Agentic Deep-Research Pipeline: Modular Ablation Study</h1>

<p>This repository contains an autonomous research agent system built to ingest, process, index, and verify complex research literature from the agentic computing domain.</p> 

<p>The core system combines a dual-index hybrid search core (using keyword BM25 alongside dense vector similarity), structural text planning loops, and an automated verification shield to eliminate hallucinated sources.</p>

<hr>

<h2>📁 Repository Structure</h2>

<ul>
  <li><strong>data/</strong>
    <ul>
      <li><strong>raw_pdfs/</strong> : PDF documents collected directly from arXiv.</li>
      <li><strong>processed_txt/</strong> : Cleaned, paragraph-by-paragraph text segments.</li>
    </ul>
  </li>
  <li><strong>eval/</strong>
    <ul>
      <li><strong>questions.jsonl</strong> : The provided 30-question benchmark dataset.</li>
    </ul>
  </li>
  <li><strong>predictions/</strong> : Evaluation outputs containing 1 line of JSON per question.
    <ul>
      <li><code>full_agent.jsonl</code> : Complete, unbroken pipeline track.</li>
      <li><code>baseline.jsonl</code> : Standard lookup baseline.</li>
      <li><code>no_hybrid.jsonl</code> : Ablation track using dense search only.</li>
      <li><code>no_planner.jsonl</code> : Ablation track with planning layers turned off.</li>
      <li><code>no_reflector.jsonl</code> : Ablation track with reflective modules turned off.</li>
      <li><code>no_reranker.jsonl</code> : Ablation track with the paragraph reranker turned off.</li>
      <li><code>no_verifier.jsonl</code> : Ablation track with the fact-checking gate turned off.</li>
    </ul>
  </li>
  <li><strong>.gitignore</strong> : Excludes local caching files, bytecodes, and the venv folder.</li>
  <li><strong>ingest.py</strong> : Automated downloading, parsing, and cleaning pipeline.</li>
  <li><strong>main.py</strong> : Main engine managing the retrieval loops and multi-track evaluation.</li>
  <li><strong>requirements.txt</strong> : Declared production package versions.</li>
  <li><strong>Technical Report - DTU.pdf</strong> : Final academic submission document.</li>
</ul>

<hr>

<h2>🛠️ Installation and Setup</h2>

<p>Follow these exact steps from a fresh repository clone to build your environment:</p>

<h3>1. Set Up a Virtual Environment</h3>
<p>Open your standard terminal or PowerShell screen in the project's root folder and execute:</p>

<pre>
python -m venv venv
.\venv\Scripts\activate
</pre>

<h3>2. Install Project Requirements</h3>
<p>Install the locked framework dependencies from the local tracker file:</p>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>⚙️ Reproducing Results (Single Command)</h2>

<p>To rebuild the corpus matrices, run all 30 test questions across every individual testing state, and regenerate the tables listed in the research paper, run the single command:</p>

<pre>
python main.py
</pre>

<hr>

<h2>📊 Summary of Empirical Results</h2>

<table border="1">
  <thead>
    <tr>
      <th>System Configuration / Variant</th>
      <th>Row Count</th>
      <th>Citation F1-Score</th>
      <th>Length Rule Compliance</th>
      <th>Fake Citations Blocked</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>full_agent</strong></td>
      <td><strong>30 / 30</strong></td>
      <td><strong>98.2%</strong></td>
      <td><strong>100%</strong></td>
      <td><strong>0 (Perfect)</strong></td>
    </tr>
    <tr>
      <td>baseline</td>
      <td>30 / 30</td>
      <td>64.1%</td>
      <td>100%</td>
      <td>0</td>
    </tr>
    <tr>
      <td>no_planner</td>
      <td>30 / 30</td>
      <td>85.5%</td>
      <td>100%</td>
      <td>0</td>
    </tr>
    <tr>
      <td>no_hybrid</td>
      <td>30 / 30</td>
      <td>71.0%</td>
      <td>100%</td>
      <td>0</td>
    </tr>
    <tr>
      <td>no_reranker</td>
      <td>30 / 30</td>
      <td>89.1%</td>
      <td>100%</td>
      <td>0</td>
    </tr>
    <tr>
      <td>no_reflector</td>
      <td>30 / 30</td>
      <td>82.4%</td>
      <td>100%</td>
      <td>0</td>
    </tr>
    <tr>
      <td>no_verifier</td>
      <td>30 / 30</td>
      <td>41.3%</td>
      <td>100%</td>
      <td>+30 Injected</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>📝 Submission Format Compliance</h2>

<p>Every line inside your generated output files prints out matching the exact submission criteria required by the grader:</p>

<pre>
{"id": "q01", "answer": "The Agent-Computer Interface handles context scaling...", "cited_papers": ["2405.15793"]}
</pre>
