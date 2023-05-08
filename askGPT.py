import openai
import argparse

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

# its a function that gets the openai response
def get_completions(prompt, model="gpt-3.5-turbo"):
	messages = [{"role": "user", "content": prompt}]
	response = openai.ChatCompletion.create(
		model=model,
		messages=messages,
		temperature=0,
	)
	return response.choices[0].message["content"]

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
api_key_group.add_argument("-A", "--add-api-key", help="add chatGPT api key")
api_key_group.add_argument("-C", "--clear-api-key", action="store_true", help="clear stored chatGPT api key")
api_key_group.add_argument("-P", "--print-api-key", action="store_true", help="print stored chatGPT api key")

api_action_group.add_argument("--ask-gpt", help="ask a question to chatGPT")

args = parser.parse_args()

if args.clear_api_key:
	clear_api_key()	
elif args.add_api_key:
	add_api_key(args.add_api_key)
elif args.print_api_key:
	print_api_key()
elif args.ask_gpt:
	ask_gpt(args.ask_gpt)


