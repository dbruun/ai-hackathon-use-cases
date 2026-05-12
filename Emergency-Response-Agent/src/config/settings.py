"""Settings configuration using Pydantic."""

from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # OpenWeatherMap API
    openweather_api_key: str = ""

    # Microsoft Foundry model configuration
    azure_openai_endpoint: str = Field(
        default="",
        validation_alias=AliasChoices("FOUNDRY_ENDPOINT", "AZURE_OPENAI_ENDPOINT"),
    )
    azure_openai_key: str = Field(
        default="",
        validation_alias=AliasChoices(
            "FOUNDRY_API_KEY", "AZURE_OPENAI_API_KEY", "AZURE_OPENAI_KEY"
        ),
    )
    azure_openai_deployment: str = Field(
        default="gpt-4",
        validation_alias=AliasChoices(
            "FOUNDRY_MODEL_DEPLOYMENT_NAME",
            "AZURE_OPENAI_DEPLOYMENT_NAME",
            "AZURE_OPENAI_DEPLOYMENT",
        ),
    )

    # Azure AI Search
    azure_search_endpoint: str = ""
    azure_search_key: str = ""
    azure_search_index: str = "historical-incidents"

    # Application settings
    flask_port: int = 5002
    use_mock_services: bool = True
    log_level: str = "INFO"

    class Config:
        """Pydantic settings configuration."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

    @property
    def has_openweather_api(self) -> bool:
        """Check if OpenWeatherMap API key is configured."""
        return bool(self.openweather_api_key and self.openweather_api_key != "your_openweather_api_key_here")

    @property
    def has_azure_openai(self) -> bool:
        """Check if Azure OpenAI is configured."""
        return bool(
            self.azure_openai_endpoint
            and self.azure_openai_key
            and "your" not in self.azure_openai_key.lower()
        )

    @property
    def has_azure_search(self) -> bool:
        """Check if Azure AI Search is configured."""
        return bool(
            self.azure_search_endpoint
            and self.azure_search_key
            and "your" not in self.azure_search_key.lower()
        )


# Global settings instance
settings = Settings()
