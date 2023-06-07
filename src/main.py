import utils
import mode
import argparse

file_path = "config.yaml"

parser = argparse.ArgumentParser(
    prog="ChatGPT Bot",
    description="A customizable chatGPT bot"
)

api_action_group = parser.add_mutually_exclusive_group()

api_action_group.add_argument("-A", "--add-api-key", 
                              help="add chatGPT api key",
                              action="store_true")
api_action_group.add_argument("-S", "--set-api-key", 
                              help="set chatGPT api key",
                              action="store_true")
api_action_group.add_argument("-R", "--reset-api-key", 
                              help="reset chatGPT api key",
                              action="store_true")
api_action_group.add_argument("--ask-gpt",
                              help="ask a question to chatGPT",
                              default=True,
                              action="store_true")

args = parser.parse_args()

if args.set_api_key:
    utils.set_key(file_path)
elif args.add_api_key:
    utils.add_key(file_path)
elif args.reset_api_key:
    utils.setup(file_path)
elif args.ask_gpt:
    mode.quick_ask(file_path)