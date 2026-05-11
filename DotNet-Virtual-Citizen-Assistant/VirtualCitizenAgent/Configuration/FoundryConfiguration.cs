namespace VirtualCitizenAgent.Configuration;

/// <summary>
/// Configuration for Azure AI Foundry model inference.
/// </summary>
public class FoundryConfiguration
{
    public const string SectionName = "Foundry";

    /// <summary>
    /// Azure AI Foundry model endpoint URL.
    /// </summary>
    public string Endpoint { get; set; } = string.Empty;

    /// <summary>
    /// Azure AI Foundry API key.
    /// </summary>
    public string ApiKey { get; set; } = string.Empty;

    /// <summary>
    /// Name of the model deployment for chat.
    /// </summary>
    public string ModelDeploymentName { get; set; } = "gpt-4o";

    /// <summary>
    /// Whether to use mock service for offline development.
    /// </summary>
    public bool UseMockService { get; set; } = true;
}
