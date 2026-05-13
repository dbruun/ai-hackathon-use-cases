# Document Eligibility Agent

AI-powered document processing system for Georgia State social services. Automatically processes eligibility documents (W-2s, pay stubs, utility bills) using Azure Document Intelligence and Microsoft Agentic Framework.

## Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Demo (Mock Mode)

No Azure services required:

```bash
python demo.py
```

### 3. Run Tests

```bash
python -m pytest tests/ -v
```

## Beginner Walkthrough (VS Code + Azure)

### A. First-time local setup in VS Code

1. Install [VS Code](https://code.visualstudio.com/) and [Python 3.11+](https://www.python.org/downloads/).
2. Install the **Python** extension in VS Code.
3. Open `Document-Eligibility-Agent` in VS Code.
4. Open VS Code terminal and run:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows PowerShell: venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
5. Validate local setup first:
   ```bash
   python demo.py
   python -m pytest tests/ -v
   ```

### B. Azure resource setup (cloud mode)

1. Sign in to [Azure Portal](https://portal.azure.com/).
2. Create an **Azure AI Document Intelligence** resource.
3. (Optional advanced flow) Create Azure AI Foundry model endpoint for additional agentic processing.
4. Add secrets to `.env`:
   - `AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT`
   - `AZURE_DOCUMENT_INTELLIGENCE_KEY`
   - `USE_MOCK_SERVICES=false`
5. Re-run:
   ```bash
   python demo.py
   ```

### C. Permissions you may need

- **Contributor** role on the target resource group/subscription to create resources.
- **Cognitive Services User** or equivalent access to call Document Intelligence.
- If using Key Vault for secrets, access to read secret values at runtime.

### D. Official documentation

- [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Azure AI Document Intelligence docs](https://learn.microsoft.com/azure/ai-services/document-intelligence/)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure RBAC overview](https://learn.microsoft.com/azure/role-based-access-control/overview)

## Features

- **Document OCR**: Extract text from scanned documents using Azure Document Intelligence
- **Intelligent Classification**: Automatically identify document types
- **Data Extraction**: Extract key fields (income, employer, dates)
- **PII Detection**: Automatic detection and masking of sensitive data
- **Confidence Scoring**: Quality metrics for extracted data
- **Eligibility Assessment**: Rule-based benefit calculations

## Supported Document Types

| Document | Fields Extracted |
|----------|-----------------|
| W-2 Forms | Wages, employer, tax year |
| Pay Stubs | Gross pay, pay period, employer |
| Utility Bills | Provider, address, amount due |
| Bank Statements | Institution, balance, transactions |
| Driver's Licenses | Name, DOB, expiration |
| Birth Certificates | Name, DOB, parents |
| Lease Agreements | Landlord, address, rent amount |

## Project Structure

```
Document-Eligibility-Agent/
├── src/
│   ├── agent/           # Processing agents
│   ├── api/             # Flask routes
│   ├── config/          # Settings
│   ├── models/          # Document models
│   ├── services/        # OCR, email, storage services
│   └── plugins/         # Microsoft Agentic Framework plugins
├── sample_documents/    # Test documents
├── static/              # Web interface assets
├── tests/               # Test suite (86 tests)
├── demo.py              # Interactive demo
└── requirements.txt
```

## Configuration

For Azure services, create a `.env` file based on `.env.example`:

```env
USE_MOCK_SERVICES=false

# Azure Document Intelligence (Required for OCR)
AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT=https://your-doc-intel.cognitiveservices.azure.com
AZURE_DOCUMENT_INTELLIGENCE_KEY=your-key
```

**Where to find these values:**
1. **Document Intelligence**: Azure Portal → Your Document Intelligence resource → Keys and Endpoint

## Eligibility Programs

- **SNAP**: Supplemental Nutrition Assistance Program
- **Medicaid**: Healthcare coverage
- **Housing Assistance**: Rental subsidies
- **HEAP**: Home Energy Assistance Program

## Tech Stack

- **Azure Document Intelligence**: OCR and document parsing
- **Microsoft Graph**: Email processing
- **Microsoft Agentic Framework**: AI orchestration
- **Microsoft Foundry Models**: Intelligent extraction
- **Flask**: Web API framework
- **Pydantic**: Data validation

## Extension Ideas

- Add support for multilingual documents and translated extraction output.
- Add human review queues for low-confidence classifications.
- Add a rules editor UI so hackathon teams can configure eligibility logic live.

## Hackathon Team

Georgia State AI Hackathon - January 2026
