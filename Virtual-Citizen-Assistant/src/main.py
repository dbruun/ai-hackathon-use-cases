"""
Virtual Citizen Assistant - Main Application
Updated for Microsoft Agentic Framework 1.37.0 and Pydantic v2 compatibility
"""
import asyncio
import os
from typing import Optional
from agent_framework import Agent
from agent_framework.openai import OpenAIChatCompletionClient
from src.plugins.document_retrieval_plugin import DocumentRetrievalPlugin
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class VirtualCitizenAssistant:
    def __init__(self):
        self.agent: Optional[Agent] = None
        self.chat_history: list[dict[str, str]] = []
        
    async def initialize(self):
        """Initialize the agent and plugins"""
        print("Initializing Virtual Citizen Assistant...")

        from src.plugins.scheduling_plugin import SchedulingPlugin
        document_plugin = DocumentRetrievalPlugin()
        scheduling_plugin = SchedulingPlugin()

        chat_client = OpenAIChatCompletionClient(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        )

        self.agent = Agent(
            client=chat_client,
            instructions="You are a helpful virtual assistant for Georgia city services.",
            tools=[
                document_plugin.search_city_services,
                document_plugin.get_service_by_category,
                scheduling_plugin.check_availability,
                scheduling_plugin.scheduling_info,
                scheduling_plugin.list_schedulable_services,
            ]
        )

        print("✅ Virtual Citizen Assistant initialized successfully!")
        print("   - DocumentRetrieval plugin loaded")
        print("   - Scheduling plugin loaded")
        
    async def chat(self, user_message: str) -> str:
        """Process a user message and return a response"""
        if not self.agent:
            raise RuntimeError("Assistant not initialized. Call initialize() first.")

        self.chat_history.append({"role": "user", "content": user_message})

        recent_history = self.chat_history[-10:]
        conversation_context = "\n".join(
            f"{message['role'].capitalize()}: {message['content']}" for message in recent_history
        )
        prompt = (
            "Use this conversation history to answer the latest user request.\n\n"
            f"{conversation_context}"
        )

        response = await self.agent.run(prompt)
        assistant_response = response.text or str(response.value)

        self.chat_history.append({"role": "assistant", "content": assistant_response})
        return assistant_response
    
    def get_chat_history(self) -> list:
        """Get the current chat history"""
        return self.chat_history

async def main():
    """Main function for testing the assistant"""
    assistant = VirtualCitizenAssistant()
    
    try:
        await assistant.initialize()
        
        print("\n" + "="*50)
        print("Virtual Citizen Assistant is ready!")
        print("You can now ask questions about city services.")
        print("Type 'quit' to exit.")
        print("="*50 + "\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Assistant: Goodbye! Have a great day!")
                break
            
            if not user_input:
                continue
            
            try:
                response = await assistant.chat(user_input)
                print(f"Assistant: {response}")
            except Exception as e:
                print(f"Assistant: I'm sorry, I encountered an error: {e}")
                
    except Exception as e:
        print(f"Failed to initialize assistant: {e}")
        print("Please check your environment variables:")
        print("- AZURE_OPENAI_ENDPOINT")
        print("- AZURE_OPENAI_API_KEY")
        print("- AZURE_OPENAI_DEPLOYMENT_NAME")
        print("- AZURE_SEARCH_ENDPOINT")
        print("- AZURE_SEARCH_KEY")
        print("- AZURE_SEARCH_INDEX")

if __name__ == "__main__":
    asyncio.run(main())
