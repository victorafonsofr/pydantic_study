#%%

from pydantic_ai import Agent
from dotenv import load_dotenv
from pydantic_ai.models.google import GoogleModel

load_dotenv('.env')

model = GoogleModel('gemini-3.8-flash')
agent = Agent(model)

# await is necessary because the api is async
#run() sends the message to your agent and awaits the response
try:
    response = agent.run_sync(
        "Which is the capital of France?"
    )

    print("Resposta:", response.output)

except Exception as e:
    print("Erro na execução:", repr(e))
#> The capital of France is Paris.
#%%