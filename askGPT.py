import openai
import argparse
from rich.console import Console
from rich.markdown import Markdown
from redline import Redlines

# its a function that clears the api key
def clear_api_key():
	name = input('Are you sure to clear the api-key? (y/n): ')
	if name != 'y':
		return
	with open('.api-key', 'w') as f:
		f.write('')
	f.close()
	print('\U0001F9F9 The chatGPT key has been cleared successfully!')

# its a function that append the added api key to the .api-key file
def add_api_key(api_key):
	with open('.api-key', 'w') as f:
		f.write(api_key)
	f.close()
	print('\U0001F600 The chatGPT key "{}" has been added successfully!'.format(api_key))

# its a function that prints the api key
def print_api_key():
	with open('.api-key', 'r') as f:
		api_key = f.read()
		if api_key == '':
			print('\U0001F62D The api-key is not set yet!')
		else:
			print('\U0001F511 The api-key is: {}'.format(api_key))


def set_api_key():
	with open('.api-key', 'r') as f:
		openai.api_key = f.read()
	f.close()

def ask_chatbot():
	context = []
	role = input("Set the role of the chatbot: \n")
	if role:
		context.append({'role':'system', 'content': f"{role}"})
	print("Input 'END' to end the conversation.")
	while True:
		prompt = input('You: ')
		if prompt == 'END':
			break
		context.append({'role': 'user', 'content': f"{prompt}"})
		response = get_completion_from_messages(context) 
		print("GPT: {}".format(response))
		context.append({'role': 'assistant', 'content': f"{response}"})

# its a function that gets the openai response
def get_completions(prompt, model="gpt-3.5-turbo"):
	messages = [{"role": "user", "content": prompt}]
	response = openai.ChatCompletion.create(
		model=model,
		messages=messages,
		temperature=0,
	)
	return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

def input_text():
	text = ''
	while True:
		user_input = input('Text: ')
		if user_input == 'END':
			break
		text += user_input + '\n'
	return text

# its a function that ask gpt questions and print the results
# !TODO: 实现流式返回
def ask_gpt(type):
	set_api_key()
	prompt = ''
	if type == 'normal':
		question = input('Question: ')
		prompt = f"""
			Question: ```{question}```
		"""
	elif type == 'inferring':
		text = input_text()
		
		topic_list = [
			"nasa", "local government", "engineering", 
			"employee satisfaction", "federal government"
		]

		prompt = f"""
		Determine whether each item in the following list of topics is a topic in the text below, which is delimited with triple backticks.
		Give your answer as list with 0 or 1 for each topic.
		Format your answer a JSON object.
		List of topics: {", ".join(topic_list)}
		Text sample: '''{text}'''
		"""

		print("prompt: {}".format(prompt))

	elif type == 'correct':
		# !TODO: 重构 correct 的写法
		text = input_text()
		prompt = f"""
		proofread and correct the review:```{text}```
		"""
		response = get_completions(prompt)
		diff = Redlines(text, response)
		markdown_text = diff.output_markdown
		print(markdown_text)	
		return
	elif type == 'chatbot':
		ask_chatbot()
		return

	if prompt == '':
		print('\U0001F62D The prompt is empty! Maybe the question type is not valid!')
	else :
		response = get_completions(prompt)
		print(response)

parser = argparse.ArgumentParser(
	prog="ChatGPT Bot",
	description="A customizable chatGPT bot"
)

api_action_group = parser.add_mutually_exclusive_group()

api_key_group = api_action_group.add_mutually_exclusive_group()
api_key_group.add_argument("-A", "--add-api-key", metavar="api-key", help="add chatGPT api key")
api_key_group.add_argument("-C", "--clear-api-key", action="store_true", help="clear stored chatGPT api key")
api_key_group.add_argument("-P", "--print-api-key", action="store_true", help="print stored chatGPT api key")

api_action_group.add_argument("--ask-gpt", metavar="question-type", help="ask a question to chatGPT")

args = parser.parse_args()

if args.clear_api_key:
	clear_api_key()	
elif args.add_api_key:
	add_api_key(args.add_api_key)
elif args.print_api_key:
	print_api_key()
elif args.ask_gpt:
	ask_gpt(args.ask_gpt)


