import json
class IokaAPI:
    def __init__(self, api_key):
        self.api_key = api_key

    @staticmethod
    def set_api_key(api_key):
        # Save the API key to a configuration file or settings module
        with open('config.json', 'w') as config_file:
            json.dump({"api_key": api_key}, config_file)

    def load_api_key():
        try:
            with open('config.json', 'r') as config_file:
                config_data = json.load(config_file)
                return config_data.get('api_key', None)
        except FileNotFoundError:
            return None




