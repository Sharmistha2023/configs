import openai
import httpx

client = openai.Client(
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWpheS1hbnRvIiwidHlwZSI6ImFwaSIsImlkIjoiL2RlcGxveW1lbnQvbnYtZW1iZWRxYS1taXN0cmFsLTdiLXYyLyJ9.w99o6iD6XwR0CbVvv0cdTJA5Gi9sg-enc7QO4y-hVW4",
    base_url="https://awsvm1:32443/deployment/published/nv-embedqa-mistral-7b-v2/v1/",
    #base_url="https://awsvm1:32443/deployment/default/bge1/v1/",
    #api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGVmYXVsdCIsInR5cGUiOiJhcGkiLCJpZCI6Ii9kZXBsb3ltZW50L2JnZTEvIn0.NRs3b7LPrK_uu_B5X446gOH8T_fH5AJ1Lfd49JtIRPI",
    #api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZGVmYXVsdCIsInR5cGUiOiJhcGkiLCJpZCI6Ii9kZXBsb3ltZW50L2JnZTQvIn0.uft8gHivX4P69MUx9rF9hfhJU1h9uSQN3qfobL_0HNM",
    #base_url="https://awsvm1:32443/skypilot/d3x/sky-serve-controller-ff7fd36f-ff7fd36f/30001/v1/",
    http_client=httpx.Client(verify=False)
)

models = client.models.list()
    # Try to get model_id from the models object
try:
    # Case 1: models.data[0].id
    model_id = models.data[0].id
except Exception as e:
    pass

try:
    # Case 2: models.model_id
    model_id = models.model_id
except Exception as e:
    pass
print(model_id)

result = client.embeddings.create(
    model=model_id,
    extra_body={"input_type": "query"},
    input=["The food was delicious and the waiter...", "India is my country, , In the quiet village of Windmere, nestled between rolling hills and thick forests, there stood a library no one remembered building.Naturally, the villagers were curious. Tom, the mailman, was the first to enter. He went in at 9:03 AM. He came out ten minutes later, looking ten years younger and clutching a notebook full of terrible poetry."],
)

embeddings = [item.embedding for item in result.data]
print(embeddings)
