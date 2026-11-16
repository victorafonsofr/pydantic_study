from pydantic_ai import Agent

agent = Agent(model='test',
                instructions='seu nome e lixo')
print(agent.description)
#> The capital of France is Paris.