# Inter-Agency Knowledge Hub

Cross-agency document search system with permission-aware results for Georgia State government. Provides unified search across multiple agency knowledge bases with role-based access control.

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
3. Open `Inter-Agency-Knowledge-Hub` in VS Code.
4. In VS Code terminal run:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows PowerShell: venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
5. Validate baseline behavior locally:
   ```bash
   python demo.py
   python -m pytest tests/ -v
   ```

### B. Azure resource setup (cloud mode)

1. Sign in to [Azure Portal](https://portal.azure.com/).
2. Create Azure AI Foundry model endpoint and deployment.
3. Create Azure AI Search service and index.
4. Register an Entra ID app for API access (tenant/client credentials).
5. Add the required keys and IDs in `.env` and set `USE_MOCK_SERVICES=false`.
6. Re-run:
   ```bash
   python demo.py
   ```

### C. Permissions you may need

- **Contributor** role for resource creation.
- **Search Service Contributor** (or equivalent) for index/data operations.
- Entra app registration permissions (or admin-created app credentials).
- Permission to invoke deployed Foundry model.

### D. Official documentation

- [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure AI Search docs](https://learn.microsoft.com/azure/search/)
- [Microsoft Entra app registration quickstart](https://learn.microsoft.com/entra/identity-platform/quickstart-register-app)
- [Azure RBAC overview](https://learn.microsoft.com/azure/role-based-access-control/overview)

## Features

- **Unified Search**: Query across 5+ agency knowledge bases
- **Permission-Aware Results**: Role-based filtering via Entra ID
- **Citation Tracking**: Source attribution for LOADinG Act compliance
- **Cross-Agency References**: Link related policies across agencies
- **Human-in-the-Loop**: Escalation for complex queries
- **7-Year Audit Logs**: Complete search and access history

## Supported Agencies

| Agency | Domain | Documents |
|--------|--------|-----------|
| DMV | Transportation | Licensing, registration |
| DOL | Labor | Employment, wages |
| OTDA | Social Services | Benefits, assistance |
| DOH | Health | Public health, regulations |
| OGS | General Services | Procurement, facilities |

## Project Structure

```
Inter-Agency-Knowledge-Hub/
├── src/
│   ├── api/             # Flask routes
│   ├── config/          # Settings
│   ├── models/          # Search models
│   ├── services/        # Search, auth services
│   └── plugins/         # Microsoft Agentic Framework plugins
├── assets/              # Sample documents
├── data/                # Index data
├── tests/               # Test suite (38 tests)
├── demo.py              # Interactive demo
└── requirements.txt
```

## Search Architecture

```
┌─────────────────────────────────────────┐
│            Search Request               │
│    (Query + User Context + Filters)     │
└───────────────────┬─────────────────────┘
                    │
         ┌──────────▼──────────┐
         │   Permission Check   │
         │   (Entra ID Groups)  │
         └──────────┬──────────┘
                    │
    ┌───────────────┼───────────────┐
    ▼               ▼               ▼
┌───────┐     ┌───────┐       ┌───────┐
│  DMV  │     │  DOL  │  ...  │  DOH  │
│ Index │     │ Index │       │ Index │
└───────┘     └───────┘       └───────┘
```

## Configuration

For Azure services, create a `.env` file based on `.env.example`:

```env
USE_MOCK_SERVICES=false

# Microsoft Foundry (Required)
FOUNDRY_ENDPOINT=https://your-foundry-resource.openai.azure.com
FOUNDRY_API_KEY=your-api-key
FOUNDRY_MODEL_DEPLOYMENT_NAME=gpt-4o
FOUNDRY_EMBEDDING_DEPLOYMENT=text-embedding-3-large

# Azure AI Search (Required)
AZURE_AI_SEARCH_ENDPOINT=https://your-search.search.windows.net
AZURE_AI_SEARCH_KEY=your-key

# Entra ID Authentication (Required for production)
AZURE_TENANT_ID=your-tenant-id
AZURE_CLIENT_ID=your-client-id
AZURE_CLIENT_SECRET=your-client-secret
```

**Where to find these values:**
1. **Foundry Models**: [Azure AI Foundry](https://ai.azure.com) → Your project → Keys and Endpoint
2. **AI Search**: Azure Portal → Your Search resource → Keys
3. **Entra ID**: Azure Portal → App registrations → Your app → Overview
4. **Deployment Name**: Azure AI Foundry → Deployments (e.g., `gpt-4o`)

## Search Modes

| Mode | Description | Best For |
|------|-------------|----------|
| Semantic | Vector similarity search | Natural language queries |
| Keyword | Traditional text matching | Exact phrases |
| Hybrid | Combined semantic + keyword | General use |

## Compliance Features

- **LOADinG Act**: Citation tracking for all AI responses
- **RAISE Act**: Transparent AI assistance disclosure
- **Audit Trail**: Complete 7-year query and access logs
- **Data Privacy**: PII masking in search results

## Tech Stack

- **Azure AI Search**: Vector and hybrid search
- **Foundry IQ**: Intelligent retrieval
- **Entra ID**: Authentication and authorization
- **Microsoft Agentic Framework**: AI orchestration
- **Flask**: Web API framework
- **Pydantic**: Data models

## Extension Ideas

- Add feedback loops to improve ranking quality from user click behavior.
- Add agency-specific copilots that summarize results in domain language.
- Add secure cross-agency sharing workflows for temporary incident collaboration.

## Hackathon Team

Georgia State AI Hackathon - January 2026
