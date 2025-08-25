import os

from dotenv import dotenv_values

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class EnvConfig:
    def __init__(self, env_file: str = None):
        self.env_file = env_file or os.path.join(base_dir, ".env")
        self._config = {}
        self._load_env_file()

    def _load_env_file(self):
        self._config = dotenv_values(self.env_file)
        for key, value in self._config.items():
            setattr(self, key, value)

    def reload(self, env_file: str = None):
        if env_file:
            self.env_file = env_file
        self._load_env_file()

    def get(self, key: str, default=None):
        return getattr(self, key, default)

    def set(self, key: str, value):
        setattr(self, key, value)
        self._config[key] = value

env_config = EnvConfig()

# print(env_config.WEATHER_API_KEY)
# print(env_config.WEATHER_INFO_URL)
# print(env_config.GEMINI_API_KEY)