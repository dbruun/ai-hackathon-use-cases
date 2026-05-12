# Inter-Agency Knowledge Hub - Step by Step Execution Guide

This guide shows how to run the project locally in mock mode first, then with Microsoft Foundry.

## 1. Open a terminal in this folder

```bash
cd Inter-Agency-Knowledge-Hub
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

## 6. Optional: run with Microsoft Foundry

Create a `.env` file in this folder and set:

```env
USE_MOCK_SERVICES=false
# Microsoft Foundry model endpoint and key
FOUNDRY_ENDPOINT=https://your-foundry-resource.openai.azure.com
FOUNDRY_API_KEY=your-foundry-api-key
FOUNDRY_MODEL_DEPLOYMENT_NAME=gpt-4o
FOUNDRY_EMBEDDING_DEPLOYMENT=text-embedding-3-large
AZURE_SEARCH_ENDPOINT=https://your-search.search.windows.net
AZURE_SEARCH_API_KEY=your-search-key
AZURE_TENANT_ID=your-tenant-id
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
```

Then run:

```bash
python demo.py
```
