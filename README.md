# hallucination-detection

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/MingxiaoZhang/hallucination-detection.git
cd hallucination-detection
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application using the command line interface

**Use standard input**

```bash
python main.py
```

**Use file input**
Create `<file_name>.json` file in folder `/test` with format 

```json
{
    "ground_truth": "<your_ground_truth>",
    "llm_output": "<your_llm_output>",
}
```

```bash
python main.py --file test/<file_name>.json
```