from pydantic_ai import Agent
from pydantic_ai.capabilities import MCP
from dotenv import load_dotenv

load_dotenv('.env')
agent = Agent(
    'google-cloud:gemini-3.8-flash',
    capabilities=[
        # Runs the MCP server locally by default
        MCP(url='https://mcp.example.com/api', native=True, local=False)
    ],
)

async def main():
    result = await agent.run("bom dia!")
    while True:
        print(f"\n{result.data}") #result.data -> resposta do agente
        user_input = input("\n$You >")
        result = await agent.run(user_input,message_history=result.new_messages())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
