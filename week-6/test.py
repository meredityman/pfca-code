import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {
	"Authorization": "Bearer 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"
}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Can you give me your honest feedback on the School of Machines ",
})

print(output)