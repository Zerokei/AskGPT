import openai

class ChatBot:
    def __init__(self, key):
        if "API_TYPE" in key:
            self.type = 'azure'
            self.api_type: str = str(key['API_TYPE'])
            self.api_base: str = str(key['API_BASE'])
            self.api_version: str = str(key['API_VERSION'])
            self.api_key: str = str(key['API_KEY'])
            self.engine = key['ENGINE']
        else: 
            self.type = 'openai'
            self.api_key = key['API_KEY']

        if self.type == 'azure':
            openai.api_type = self.api_type
            openai.api_base = self.api_base
            openai.api_version = self.api_version
            openai.api_key = self.api_key
            print("Azure API has been set up successfully!")
        else: 
            openai.api_key = self.api_key
    def chat(self, prompt):
        message = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            engine = self.engine,
            messages = message,
            stream = True,
        )
        for event in response:
            event_text = event['choices'][0]['delta'].get('content', '')
            yield event_text