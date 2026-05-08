# Georgia Virtual Citizen Assistant

[![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)](#)
[![Tests](https://img.shields.io/badge/Tests-22%20Passing-brightgreen.svg)](#running-tests)
[![.NET 9](https://img.shields.io/badge/.NET-9.0-512BD4.svg)](https://dotnet.microsoft.com)

A RAG-powered AI assistant for Georgia government services built with .NET 9, Microsoft Agentic Framework, Azure AI Foundry, and Azure AI Services.

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
- Azure AI Foundry model endpoint (optional - mock mode available)

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
1. Go to [Azure AI Foundry](https://ai.azure.com) → Your model endpoint resource
2. **Keys and Endpoint** → Copy Endpoint and Key
3. **Model deployments** in Azure AI Studio → Note your deployment name (e.g., `gpt-4o`)

### 3. Upload Documents (Optional)

```bash
cd AzureSearchUploader
dotnet run
```

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
- **Azure AI Foundry Models** - Chat completions
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
│ Azure AI Foundry│
│ + Agentic Framework │
└─────────────────┘
```

## Hackathon Team

Georgia State AI Hackathon - January 2026
