import core
import yaml

def quick_ask(file_path):
    with open(file_path, 'r') as f:
        dict = yaml.load(f, Loader=yaml.FullLoader)
    chatbot = core.ChatBot(dict['KEYS'][dict['USE']])
    while True:
        prompt = input("\U0001F600 You: ")
        print("\U0001F916 GPT: ", end="")
        for item in chatbot.chat(prompt):
            print(item, end="")
        print("")