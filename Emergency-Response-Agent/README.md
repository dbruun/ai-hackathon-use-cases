# Emergency Response Agent

Multi-agent AI system for emergency response planning and coordination. Generates coordinated response plans across multiple Georgia State agencies using weather data integration and resource management.

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
3. Open `Emergency-Response-Agent` in VS Code.
4. In the VS Code terminal:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows PowerShell: venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
5. Run locally in mock mode first:
   ```bash
   python demo.py
   ```

### B. Azure resource setup (cloud mode)

1. Sign in to [Azure Portal](https://portal.azure.com/).
2. Create Azure AI Foundry model endpoint and deploy a model (for example `gpt-4o`).
3. Confirm weather API endpoint (default: `https://api.weather.gov`).
4. Create `.env` and set:
   - `FOUNDRY_ENDPOINT`
   - `FOUNDRY_API_KEY`
   - `FOUNDRY_MODEL_DEPLOYMENT_NAME`
   - `USE_MOCK_SERVICES=false`
5. Run again:
   ```bash
   python demo.py
   ```

### C. Permissions you may need

- **Contributor** role (or equivalent) to create Azure resources.
- Access to invoke your deployed model endpoint.
- Network/security approval if your org restricts outbound API traffic.

### D. Official documentation

- [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Azure RBAC overview](https://learn.microsoft.com/azure/role-based-access-control/overview)
- [National Weather Service API docs](https://www.weather.gov/documentation/services-web-api)

## Features

- **Emergency Scenario Simulation**: Hurricane, fire, flood, winter storm, public health, earthquake
- **Multi-Agent Orchestration**: Coordinated planning across specialized AI agents
- **Real-time Weather Integration**: NWS API for weather threat assessment
- **Resource Coordination**: Track and allocate resources across agencies
- **Evacuation Planning**: Route optimization with bottleneck analysis
- **Historical Analysis**: Learn from past incident responses

## Emergency Types Supported

| Type | Lead Agency | Key Resources |
|------|-------------|---------------|
| Hurricane | OEM | Evacuation, shelters |
| Fire | FDNY | Firefighters, equipment |
| Flooding | OEM | Pumps, rescue boats |
| Winter Storm | DOT | Plows, salt trucks |
| Public Health | DOH | Healthcare workers, vaccines |
| Earthquake | OEM | Search & rescue teams |
| Infrastructure | Utilities | Emergency generators |

## Project Structure

```
Emergency-Response-Agent/
├── src/
│   ├── agents/          # Specialized AI agents
│   ├── api/             # Flask routes
│   ├── config/          # Settings
│   ├── models/          # Emergency models
│   ├── orchestration/   # Multi-agent coordinator
│   └── services/        # Weather, traffic APIs
├── assets/              # Static resources
├── static/              # Web interface
├── tests/               # Test suite (62 tests)
├── demo.py              # Interactive demo
└── requirements.txt
```

## Multi-Agent Architecture

```
┌─────────────────────────────────────────┐
│           Orchestration Agent           │
│    (Coordinates all response agents)    │
└─────────────────────────────────────────┘
         │           │           │
         ▼           ▼           ▼
    ┌─────────┐ ┌─────────┐ ┌─────────┐
    │ Weather │ │Resource │ │Logistics│
    │  Agent  │ │  Agent  │ │  Agent  │
    └─────────┘ └─────────┘ └─────────┘
```

## Configuration

For Azure services, create a `.env` file based on `.env.example`:

```env
USE_MOCK_SERVICES=false

# Microsoft Foundry (Required)
FOUNDRY_ENDPOINT=https://your-foundry-resource.openai.azure.com
FOUNDRY_API_KEY=your-api-key
FOUNDRY_MODEL_DEPLOYMENT_NAME=gpt-4o

# Weather API (Optional - has free tier)
NWS_API_ENDPOINT=https://api.weather.gov
```

**Where to find these values:**
1. Go to [Azure AI Foundry](https://ai.azure.com) → Your Foundry project
2. **Keys and Endpoint** → Copy Endpoint and Key
3. **Model deployments** → Note your deployment name (e.g., `gpt-4o`)

## Coordinated Agencies

- **OEM**: Office of Emergency Management
- **FDNY**: Fire Department
- **NYPD**: Police Department
- **DOT**: Department of Transportation
- **MTA**: Metropolitan Transit Authority
- **DOH**: Department of Health

## Tech Stack

- **Microsoft Agentic Framework**: Multi-agent orchestration
- **Microsoft Foundry Models**: Planning and analysis
- **NWS API**: Weather data integration
- **Flask**: Web API framework
- **Pydantic**: Data models

## Extension Ideas

- Add geospatial mapping for shelters, closures, and evacuation zones.
- Add simulation playback to compare alternative response plans.
- Add SMS/email alert integrations for citizen and agency notifications.

## Hackathon Team

Georgia State AI Hackathon - January 2026
