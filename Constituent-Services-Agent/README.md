# Constituent Services Agent

AI-powered conversational agent for Georgia State constituent services. Provides accurate, citation-backed answers about government services with multi-language support.

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

### 3. Run Web Interface

```bash
python -m src.main
```

Open http://localhost:5000 in your browser.

## Beginner Walkthrough (VS Code + Azure)

### A. First-time local setup in VS Code

1. Install [VS Code](https://code.visualstudio.com/) and [Python 3.11+](https://www.python.org/downloads/).
2. In VS Code, install the **Python** extension from Microsoft.
3. Open this folder in VS Code: `Constituent-Services-Agent`.
4. Open a new terminal in VS Code (**Terminal → New Terminal**).
5. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows PowerShell: venv\Scripts\Activate.ps1
   ```
6. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
7. Run in mock mode first (no Azure needed):
   ```bash
   python demo.py
   python -m src.main
   ```

### B. Azure resource setup (cloud mode)

1. Sign in to the [Azure Portal](https://portal.azure.com/) with a subscription where you can create resources.
2. Create an Azure AI Foundry project/model endpoint and deploy a chat model (for example `gpt-4o`).
3. Copy your endpoint, key, and deployment name into `.env`.
4. Set `USE_MOCK_SERVICES=false` and restart the app.

### C. Permissions you may need

- **Subscription/Resource Group access**: `Contributor` (or equivalent) to create resources.
- **Model inference access**: permission to use the deployed Azure OpenAI/Foundry model.
- If your team uses managed identities, grant the app identity access to the model endpoint.

### D. Official documentation

- [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure role-based access control (RBAC)](https://learn.microsoft.com/azure/role-based-access-control/overview)

## Features

- **Basic Q&A**: Ask questions about Georgia State services in plain language
- **Citation Support**: All responses include source citations
- **Confidence Scoring**: Shows confidence level for responses
- **Escalation**: Offers human agent escalation when confidence is low
- **WCAG 2.1 AA**: Accessible web interface

## Demo Scenarios

Try these queries:

1. "How do I apply for SNAP benefits?"
2. "How do I renew my driver's license?"
3. "How do I file for unemployment?"
4. "Am I eligible for Medicaid?"

## Project Structure

```
Constituent-Services-Agent/
├── src/
│   ├── agent/           # AI agent components
│   ├── api/             # Flask routes
│   ├── config/          # Settings
│   ├── models/          # Data models
│   └── services/        # External integrations
├── static/              # Web interface
├── sample_data/         # Mock agency data
├── tests/               # Test suite
├── demo.py              # Demo script
└── requirements.txt
```

## Configuration

For Azure services, create a `.env` file based on `.env.example`:

```env
USE_MOCK_SERVICES=false

# Microsoft Foundry (Required)
FOUNDRY_ENDPOINT=https://your-foundry-resource.openai.azure.com
FOUNDRY_API_KEY=your-api-key
FOUNDRY_MODEL_DEPLOYMENT_NAME=gpt-4o

# Azure AI Foundry (Optional)
AZURE_AI_PROJECT_CONNECTION_STRING=your-connection-string
```

**Where to find these values:**
1. Go to [Azure AI Foundry](https://ai.azure.com) → Your Foundry project
2. **Keys and Endpoint** → Copy Endpoint and Key
3. **Model deployments** → Note your deployment name (e.g., `gpt-4o`)

## Agency Coverage

- **DMV**: Driver licenses, vehicle registration, REAL ID
- **DOL**: Unemployment insurance, paid family leave
- **OTDA**: SNAP, HEAP, Medicaid

## Extension Ideas

- Add support for additional languages and localization.
- Integrate live agency APIs for real-time service status and wait times.
- Add analytics dashboards for unanswered questions and escalation trends.

## Hackathon Team

Georgia State AI Hackathon - January 2026
