# QA Annotator Tool

This is a simple **Question-Answer (QA) Annotator Tool** built with **Flask**. The tool allows users to annotate QA pairs for a given set of passages in **JSON format**. The dataset consists of passages with titles and contexts, and you can annotate each passage with a question and an answer span.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/j-ranasinghe/qa_annotator.git]
   cd qa-annotator

2. **Create a virtual environment (optional but recommended)**:
    ```
    python3 -m venv venv
    source venv\Scripts\activate
    ```
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt

4. Run the Flask app:
   ```
   flask run
