# DotNet Virtual Citizen Assistant - Step by Step Execution Guide

This guide shows how to run the .NET accelerator in mock mode first, then with Microsoft Foundry.

## 1. Open a terminal in this folder

```bash
cd DotNet-Virtual-Citizen-Assistant
```

## 2. Restore dependencies

```bash
dotnet restore
```

## 3. Run in mock mode (no Azure required)

```bash
dotnet run --project VirtualCitizenAgent
```

Open: http://localhost:5000

## 4. Run tests

```bash
dotnet test
```

## 5. Optional: run with Microsoft Foundry and Azure AI Search

Option A: update `VirtualCitizenAgent/appsettings.json`.

Set:
- `Foundry.Endpoint`
- `Foundry.ApiKey`
- `Foundry.ModelDeploymentName`
- `Foundry.UseMockService=false`
- `SearchConfiguration.Endpoint`
- `SearchConfiguration.ApiKey`
- `SearchConfiguration.UseMockService=false`

Option B: set environment variables in PowerShell:

```powershell
$env:Foundry__Endpoint = "https://your-foundry-resource.services.ai.azure.com"
$env:Foundry__ApiKey = "your-api-key"
$env:Foundry__ModelDeploymentName = "gpt-4o"
$env:Foundry__UseMockService = "false"
$env:SearchConfiguration__Endpoint = "https://your-search.search.windows.net"
$env:SearchConfiguration__ApiKey = "your-search-key"
$env:SearchConfiguration__UseMockService = "false"
```

Then run:

```bash
dotnet run --project VirtualCitizenAgent
```

## 6. Optional: upload sample documents to Search

```bash
dotnet run --project AzureSearchUploader
```
