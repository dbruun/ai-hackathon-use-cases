# Policy Compliance Checker

AI-powered automated review of policy documents against compliance rules for Georgia State agencies. Analyzes documents for regulation compliance and generates detailed reports with recommendations.

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
2. Install the **Python** extension.
3. Open `Policy-Compliance-Checker` in VS Code.
4. In the VS Code terminal run:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows PowerShell: venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
5. Validate local mock execution:
   ```bash
   python demo.py
   python -m pytest tests/ -v
   ```

### B. Azure resource setup (cloud mode)

1. Sign in to [Azure Portal](https://portal.azure.com/).
2. Open [Microsoft Foundry](https://ai.azure.com/) and create/select your project.
3. Use Microsoft Foundry **Model catalog** to compare models for policy analysis:
   - Cost/token usage
   - Latency and response quality
   - Context length for long policy documents
4. Deploy the selected model in **Deployments** and wait for status **Succeeded**.
5. Create agents in either mode:
   - **UI path**: Microsoft Foundry → **Agents** → Create agent → select deployed model and add compliance instructions.
   - **Code path**: extend Microsoft Agentic Framework plugin code in `src/plugins/` and service logic in `src/services/`.
6. Add values to `.env`:
   - `FOUNDRY_ENDPOINT`
   - `FOUNDRY_API_KEY`
   - `FOUNDRY_MODEL_DEPLOYMENT_NAME`
   - `USE_MOCK_SERVICES=false`
7. Re-run the demo.

### C. Permissions you may need

- **Contributor** role to create resources.
- Permission to call the Foundry/OpenAI deployment.
- Optional Key Vault access if your team stores secrets outside `.env`.

### D. Official documentation

- [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Microsoft Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Microsoft Foundry model catalog and model selection](https://learn.microsoft.com/azure/ai-foundry/concepts/models-overview)
- [Microsoft Agentic Framework documentation](https://learn.microsoft.com/agent-framework/)
- [Azure RBAC overview](https://learn.microsoft.com/azure/role-based-access-control/overview)

## Features

- **Document Parsing**: Support for PDF, DOCX, Markdown, and plain text
- **Rule-Based Checking**: Pattern matching with configurable compliance rules
- **AI-Powered Analysis**: Deep content analysis using Microsoft Foundry Models
- **Severity Classification**: Critical, High, Medium, Low categorization
- **Compliance Scoring**: 0-100 score with detailed breakdown
- **Recommendations**: Actionable guidance for each violation
- **Version Comparison**: Track policy changes over time

## Supported Document Types

| Format | Extension | Parser |
|--------|-----------|--------|
| PDF | .pdf | pypdf |
| Word | .docx | python-docx |
| Markdown | .md | Built-in |
| Plain Text | .txt | Built-in |

## Project Structure

```
Policy-Compliance-Checker/
├── src/
│   ├── api/             # Flask routes
│   ├── config/          # Settings
│   ├── models/          # Compliance models
│   ├── services/        # Rule engine, parsing
│   └── plugins/         # Microsoft Agentic Framework plugins
├── assets/              # Sample documents
├── tests/               # Test suite (14 tests)
├── demo.py              # Interactive demo
└── requirements.txt
```

## Compliance Categories

| Category | Description | Examples |
|----------|-------------|----------|
| Data Privacy | PII handling rules | Encryption, retention |
| Accessibility | WCAG compliance | Alt text, contrast |
| Security | Security standards | Authentication, logging |
| Documentation | Policy requirements | Version control, approval |

## Configuration

For Azure services, create a `.env` file based on `.env.example`:

```env
USE_MOCK_SERVICES=false

# Microsoft Foundry (Required)
FOUNDRY_ENDPOINT=https://your-foundry-resource.openai.azure.com
FOUNDRY_API_KEY=your-api-key
FOUNDRY_MODEL_DEPLOYMENT_NAME=gpt-4o
```

**Where to find these values:**
1. Go to [Microsoft Foundry](https://ai.azure.com) → Your Foundry project
2. **Keys and Endpoint** → Copy Endpoint and Key
3. **Model deployments** → Note your deployment name (e.g., `gpt-4o`)

## Sample Output

```json
{
  "document": "policy-draft.md",
  "compliance_score": 72,
  "violations": [
    {
      "rule": "DATA_RETENTION",
      "severity": "high",
      "location": "Section 3.2",
      "recommendation": "Add data retention period specification"
    }
  ]
}
```

## Tech Stack

- **Microsoft Foundry Models**: AI-powered analysis
- **Microsoft Agentic Framework**: AI orchestration
- **pypdf**: PDF parsing
- **python-docx**: Word document parsing
- **Flask**: Web API framework
- **Pydantic**: Data validation

## Extension Ideas

- Add a policy lifecycle workflow (draft → review → approval).
- Add policy diff visualizations to explain compliance score changes over time.
- Add export options for audit packages (PDF, CSV, signed reports).

## Hackathon Team

Georgia State AI Hackathon - January 2026
