📄 Resume Parser & Job Matcher (Python)
📌 Problem Statement
Recruiters and job portals often deal with unstructured resume data (PDFs) that is difficult to process programmatically.
This project solves the problem of extracting, cleaning, and structuring resume information so it can be matched against job requirements in a consistent and reliable way.
The focus of this project is:
   Handling unstructured input data
   Building a clean and reusable data-processing pipeline
   Producing structured outputs that can be used by other systems

🧠 Architecture Overview
The application is designed as a modular Python pipeline, where each stage has a clear responsibility.
1.Input Layer
  Accepts resume PDFs as input
2.Parsing Layer
  Extracts raw text from PDFs
  Handles noisy and inconsistent formatting
3.Processing Layer
  Cleans and normalizes text
  Extracts relevant entities such as skills and keywords
4.Matching Layer
   Compares processed resume data with job criteria
   Generates a structured match score/output
Each module is independent, making the system easy to debug, test, and extend.

📁 Folder Structure (Why it exists)
resume_matcher/
│
├── main.py              # Application entry point
├── parser/              # PDF text extraction logic
├── processor/           # Text cleaning and normalization
├── matcher/             # Resume-to-job matching logic
├── data/                # Sample input and output files
├── utils/               # Reusable helper functions
└── requirements.txt     # Project dependencies
Why this structure?
Separates parsing, processing, and matching concerns
Makes each component independently testable
Allows future replacement of any module without affecting others

🔐 Design & Engineering Decisions
Data Cleaning & Normalization
   Raw text extracted from PDFs is inconsistent
Normalization ensures:
     Uniform casing
     Removal of noise and redundant symbols
     Better downstream matching accuracy
Reusability
   Core logic is written as reusable functions
   Enables easy integration with:
      Web applications
      APIs
      Batch-processing systems
Maintainability
   Clear function boundaries
   Minimal hard-coding
   Logical module separation
Scalability Considerations
   New matching strategies can be added without changing the parser
   Additional input formats (DOCX, TXT) can be supported easily

▶️ How to Run the Project Locally
1.Clone the repository:
   git clone https://github.com/ballepallirakesh/resume_matcher.git
   cd resume_matcher
2.Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
3.Install dependencies:
   pip install -r requirements.txt
4.Run the application:
  python main.py

📈 Learning Outcomes
   Built a structured data-processing pipeline in Python
   Worked with unstructured input and text normalization
   Improved modular design and code readability
   Strengthened ability to explain design and logic decisions clearly

