from stored_agent import StoredAgent

def test_stored_agent():
    my_agent = StoredAgent(id='agent1', name='My Agent', storage_backend='osfs://.')
    response = my_agent.invoke(input='Hello, how are you?')
    print(response)
    assert response == 'Hello, how are you?'

def test_stored_agent_s3():
    my_agent = StoredAgent(id='agent1', name='My Agent', storage_backend='s3://cloudmatica/agents/')
    response = my_agent.invoke(input='Hello, how are you?')
    print(response)
    assert response == 'Hello, how are you?'