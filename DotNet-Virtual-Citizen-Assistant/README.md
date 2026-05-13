# Georgia Virtual Citizen Assistant

[![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)](#)
[![Tests](https://img.shields.io/badge/Tests-22%20Passing-brightgreen.svg)](#running-tests)
[![.NET 9](https://img.shields.io/badge/.NET-9.0-512BD4.svg)](https://dotnet.microsoft.com)

A RAG-powered AI assistant for Georgia government services built with .NET 9, Microsoft Agentic Framework, Microsoft Foundry, and Azure AI Services.

## Features

- **AI Chat Assistant**: Conversational interface with source citations
- **Document Search**: Semantic, keyword, and hybrid search modes
- **Category Browser**: Visual grid layout for service categories
- **Document Details**: Full content view with print and share
- **Data Upload Utility**: Batch upload documents to Azure AI Search

## Project Structure

```
DotNet-Virtual-Citizen-Assistant/
├── VirtualCitizenAgent/           # Main web application
│   ├── Controllers/               # MVC and API controllers
│   ├── Models/                    # Data models
│   ├── Services/                  # Business logic + Agentic Framework orchestration
│   ├── Views/                     # Razor views
│   └── wwwroot/                   # Static assets
├── AzureSearchUploader/           # Data upload utility
│   ├── Models/                    # Upload models
│   ├── Services/                  # Upload service
│   └── Data/                      # Sample JSON data
└── VirtualCitizenAgent.Tests/     # Unit and integration tests
```

## Prerequisites

- .NET 9.0 SDK
- Azure AI Search (optional - mock mode available)
- Microsoft Foundry model endpoint (optional - mock mode available)

## Quick Start

### 1. Run in Mock Mode (No Azure Required)

```bash
cd DotNet-Virtual-Citizen-Assistant
dotnet restore
dotnet run --project VirtualCitizenAgent
```

Open http://localhost:5000 in your browser.

### 2. Configure Azure Services (Optional)

**Option A: Edit appsettings.json**

Edit `VirtualCitizenAgent/appsettings.json`:

```json
{
  "SearchConfiguration": {
    "Endpoint": "https://your-search.search.windows.net",
    "IndexName": "citizen-services",
    "ApiKey": "your-search-api-key",
    "UseMockService": false
  },
  "Foundry": {
    "Endpoint": "https://your-foundry-resource.services.ai.azure.com",
    "ApiKey": "your-foundry-api-key",
    "ModelDeploymentName": "gpt-4o",
    "UseMockService": false
  }
}
```

**Option B: Use Environment Variables**

```powershell
# Windows PowerShell
$env:Foundry__Endpoint = "https://your-foundry-resource.services.ai.azure.com"
$env:Foundry__ApiKey = "your-api-key"
$env:Foundry__ModelDeploymentName = "gpt-4o"
$env:Foundry__UseMockService = "false"
$env:SearchConfiguration__Endpoint = "https://your-search.search.windows.net"
$env:SearchConfiguration__ApiKey = "your-search-key"
$env:SearchConfiguration__UseMockService = "false"
```

```bash
# Mac/Linux
export Foundry__Endpoint="https://your-foundry-resource.services.ai.azure.com"
export Foundry__ApiKey="your-api-key"
export Foundry__ModelDeploymentName="gpt-4o"
export Foundry__UseMockService="false"
```

**Where to find these values:**
1. Go to [Microsoft Foundry](https://ai.azure.com) → Your model endpoint resource
2. **Keys and Endpoint** → Copy Endpoint and Key
3. **Model deployments** in Azure AI Studio → Note your deployment name (e.g., `gpt-4o`)

### 3. Upload Documents (Optional)

```bash
cd AzureSearchUploader
dotnet run
```

## Beginner Walkthrough (VS Code + Azure)

### A. First-time local setup in VS Code

1. Install [VS Code](https://code.visualstudio.com/) and [.NET 9 SDK](https://dotnet.microsoft.com/download/dotnet/9.0).
2. Install the **C# Dev Kit** extension in VS Code.
3. Open `DotNet-Virtual-Citizen-Assistant` in VS Code.
4. Open a VS Code terminal and run:
   ```bash
   dotnet restore
   dotnet test
   dotnet run --project VirtualCitizenAgent
   ```
5. Open `http://localhost:5000` and verify the app loads in mock mode.

### B. Azure resource setup (cloud mode)

1. Sign in to [Azure Portal](https://portal.azure.com/).
2. Open [Microsoft Foundry](https://ai.azure.com/) and create/select a project.
3. Use Microsoft Foundry **Model catalog** to compare models by cost, latency, quality, and context length for your assistant use case.
4. Deploy a model in **Deployments**:
   - Select model/version and region
   - Set deployment name (for example `gpt-4o`)
   - Wait for status **Succeeded**
5. Create Azure AI Search service and index (`citizen-services` or your custom name).
6. Create agents in either path:
   - **UI path**: Microsoft Foundry → **Agents** → Create agent → select your deployed model and tools/knowledge.
   - **Code path**: update `VirtualCitizenAgent` configuration and extend orchestration in `VirtualCitizenAgent/Services/`.
7. Update `VirtualCitizenAgent/appsettings.json` or use environment variables from this README.
8. Set `UseMockService=false` for Foundry and Search configuration.
9. Run again:
   ```bash
   dotnet run --project VirtualCitizenAgent
   ```

### C. Permissions you may need

- **Contributor** role to create resources.
- **Search Service Contributor** (or equivalent) for index operations.
- Permission to call your Foundry/OpenAI deployment.
- If deploying the web app to Azure, rights to create App Service and assign managed identity roles.

### D. Official documentation

- [VS Code for C# development](https://code.visualstudio.com/docs/csharp/get-started)
- [Microsoft Foundry documentation](https://learn.microsoft.com/azure/ai-foundry/)
- [Microsoft Foundry model catalog and model selection](https://learn.microsoft.com/azure/ai-foundry/concepts/models-overview)
- [Azure AI Search docs](https://learn.microsoft.com/azure/search/)
- [Azure App Service deployment for ASP.NET Core](https://learn.microsoft.com/azure/app-service/quickstart-dotnetcore)
- [Microsoft Agentic Framework documentation](https://learn.microsoft.com/agent-framework/)
- [Azure RBAC overview](https://learn.microsoft.com/azure/role-based-access-control/overview)

## API Endpoints

### Chat
- `POST /api/chat` - Send a message
- `POST /api/chat/session` - Create a session
- `GET /api/chat/session/{id}` - Get session history
- `DELETE /api/chat/session/{id}` - Delete a session

### Search
- `GET /api/search?query={query}` - Search documents
- `GET /api/search/semantic?query={query}` - Semantic search
- `GET /api/search/documents/{id}` - Get document by ID
- `GET /api/search/documents/recent` - Get recent documents

### Categories
- `GET /api/categories` - List all categories
- `GET /api/categories/{name}` - Get category details

### Health
- `GET /api/health` - Health check
- `GET /api/health/ready` - Readiness check

## Running Tests

```bash
cd DotNet-Virtual-Citizen-Assistant
dotnet test
```

## Technology Stack

- **.NET 9.0** - Web framework
- **ASP.NET Core MVC** - Web application
- **Microsoft Agentic Framework 1.65** - AI orchestration
- **Azure AI Search** - Document search
- **Microsoft Foundry Models** - Chat completions
- **Bootstrap 5.3** - UI framework
- **Font Awesome 6** - Icons
- **xUnit + FluentAssertions** - Testing (22 tests)

## Architecture

```
┌─────────────────┐     ┌──────────────────┐
│   Browser       │────▶│  ASP.NET Core    │
└─────────────────┘     │     MVC          │
                        └────────┬─────────┘
                                 │
         ┌───────────────────────┼───────────────────────┐
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│  ChatService    │   │  SearchService  │   │ CategoryService │
└────────┬────────┘   └────────┬────────┘   └────────┬────────┘
         │                     │                     │
         │                     ▼                     │
         │            ┌─────────────────┐            │
         └───────────▶│ Azure AI Search │◀───────────┘
                      └─────────────────┘
         │
         ▼
┌─────────────────┐
│ Microsoft Foundry│
│ + Agentic Framework │
└─────────────────┘
```

## Extension Ideas

- Add multilingual chat with automatic translation and locale-aware citations.
- Add proactive recommendations based on user intent and service category.
- Add an admin dashboard for search quality, latency, and unanswered intents.

## Hackathon Team

Georgia State AI Hackathon - January 2026
