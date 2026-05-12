# Document Eligibility Agent - Step by Step Execution Guide

This guide shows how to run the project locally in mock mode first, then with Microsoft Foundry.

## 1. Open a terminal in this folder

```bash
cd Document-Eligibility-Agent
```

## 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

Mac/Linux:

```bash
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run demo in mock mode (no Azure required)

```bash
python demo.py
```

## 5. Run tests

```bash
python -m pytest tests/ -v
```

## 6. Optional: run with cloud services

Create a `.env` file in this folder and set:

```env
USE_MOCK_SERVICES=false
AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT=https://your-doc-intel.cognitiveservices.azure.com
AZURE_DOCUMENT_INTELLIGENCE_KEY=your-doc-intel-key
```

This accelerator does not currently require a Foundry model key in its default flow.

Then run again:

```bash
python demo.py
```
