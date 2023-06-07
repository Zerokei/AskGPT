import os
import yaml

def setup_azure():
    api_key = input("\U0001F511 API key: ")
    api_base = input("\U0001F517 API endpoint: ")
    engine = input("\U0001F916 Model name: ")
    data = {
        'API_TYPE': 'azure',
        'API_BASE': api_base,
        'API_VERSION': '2023-05-15',
        'API_KEY': api_key,
        'ENGINE': engine
    }
    return data


def setup_openai():
    api_key = input("\U0001F511 API key: ")
    data = {
        'API_KEY': api_key
    }
    return data
    

def add_key(file_path):
    with open(file_path, 'r') as f:
        dict = yaml.load(f, Loader=yaml.FullLoader)

    name = input("\U0001F48E Key name: ")
    while(True):
        print("Which API do you want to use? (Azure/OpenAI)")
        api = input("API: ")
        if api == 'Azure':
            data = setup_azure()
            break
        elif api == 'OpenAI':
            data = setup_openai()
            break
        else:
            print("Please input a valid API name.")

    dict['KEYS'][name] = data
    with open(file_path, 'w') as f:
        yaml.dump(dict, f)
    print("\U0001F389 The key has been added successfully!")

def setup(file_path):
    dict = {
        'USE': {},
        'KEYS': {}
    }

    with open(file_path, 'w') as f:
        yaml.dump(dict, f)


def set_key(file_path):
    print("Choose a key to use: ")
    with open(file_path, 'r') as f:
        dict = yaml.load(f, Loader=yaml.FullLoader)
    for key in dict['KEYS']:
        print("\U0001F511 {}".format(key))
    while True:
        key = input("Key: ")
        if key not in dict['KEYS']:
            print("Please input a valid key name.")
        else:
            dict['USE'] = key
            break
    with open(file_path, 'w') as f:
        yaml.dump(dict, f) 
    print("\U0001F389 The key has been set successfully!")