import requests


class ModelsBot():
    
    def chatbot(ex):
        url = "https://chatgpt-api8.p.rapidapi.com/"
        
        example = ex.replace("AI", "")
        query = example.splitlines()[1]
        
        payload = [
			{
				"content": query,
				"role": "user"
			}
		]
                
        headers = {
			"content-type": "application/json",
			"X-RapidAPI-Key":"384789f9dcmsh28595d5bbb1b670p100968jsnc4262f499204",
			"X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
		}
        
        response = requests.post(url, json=payload, headers=headers)
        
        return response.json()['text']