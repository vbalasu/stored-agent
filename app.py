from stored_agent import StoredAgent

my_agent = StoredAgent(id='agent1', name='My Agent')
response = my_agent.invoke(input='Hello, how are you?')
print(response)
