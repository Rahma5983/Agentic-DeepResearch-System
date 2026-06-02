import os
import arxiv
import pypdf
from urllib.request import urlretrieve

# A list of core paper arXiv IDs referenced in your evaluation sheet
TARGET_PAPERS = {
    "2408.00001": "Mem0 / Graph Memory",
    "2406.12045": "Tau-bench",
    "2404.07972": "OSWorld",
    "2405.15793": "SWE-agent"
}

def download_paper(arxiv_id, title_hint, output_dir="data/raw_pdfs"):
    """Downloads a specific paper from arXiv by its ID using version 4.0.0 API rules."""
    os.makedirs(output_dir, exist_ok=True)
    pdf_path = os.path.join(output_dir, f"{arxiv_id}.pdf")
    
    if os.path.exists(pdf_path):
        print(f"File already exists, skipping download: {pdf_path}")
        return pdf_path

    print(f"Searching arXiv for {title_hint} (ID: {arxiv_id})...")
    
    client = arxiv.Client()
    search = arxiv.Search(id_list=[arxiv_id])
    
    try:
        results_generator = client.results(search)
        paper = next(results_generator)
        
        print(f"Downloading PDF for: '{paper.title}'...")
        urlretrieve(paper.pdf_url, pdf_path)
        return pdf_path
    except Exception as e:
        print(f"Error downloading paper {arxiv_id}: {e}")
        return None

def extract_text_from_pdf(pdf_path, output_dir="data/processed_txt"):
    """Extracts text page-by-page from a PDF and saves it as a text file."""
    if not pdf_path or not os.path.exists(pdf_path):
        return
        
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.basename(pdf_path).replace(".pdf", ".txt")
    txt_path = os.path.join(output_dir, base_name)

    if os.path.exists(txt_path):
        print(f"Text file already exists, skipping extraction: {txt_path}")
        return

    print(f"Extracting text from {pdf_path}...")
    try:
        reader = pypdf.PdfReader(pdf_path)
        full_text = []
        
        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            full_text.append(f"--- PAGE {page_num + 1} ---\\n{text}")
            
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write("\n\n".join(full_text))
        print(f"Saved processed text to: {txt_path}")
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")

def run_pipeline():
    print("--- STARTING BATCH INGESTION ---")
    for arxiv_id, title_hint in TARGET_PAPERS.items():
        pdf_file = download_paper(arxiv_id, title_hint)
        if pdf_file:
            extract_text_from_pdf(pdf_file)
    print("--- INGESTION COMPLETED ---")

if __name__ == "__main__":
    run_pipeline()
