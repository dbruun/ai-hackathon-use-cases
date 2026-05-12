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
1. Go to [Azure AI Foundry](https://ai.azure.com) → Your Foundry project
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

## Hackathon Team

Georgia State AI Hackathon - January 2026
