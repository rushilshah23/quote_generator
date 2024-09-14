import os
from dotenv import load_dotenv

def get_env_dir_path():
    """Returns env dir path of the app"""
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    env_path = os.path.join(root_path, "envs")
    print(f"ENv path - {env_path}")
    return env_path


def get_environment():
    """Get enviornemnt from flask env whether PROD, DEV Or TEST"""
    env_dir_path = get_env_dir_path()
    flask_env_path = os.path.join(env_dir_path,".flaskenv")
    print(f"FLaks env - {flask_env_path}")
    load_dotenv(flask_env_path)
    return os.environ.get("ENVIRONMENT")




def load_config():
    environment = get_environment()
    env_path = get_env_dir_path()
    print(f"Environment - {environment}")
    if environment == 'PRODUCTION':
        env_file = os.path.join(env_path, ".env.prod")
    elif environment == 'DEVELOPMENT':
        env_file = os.path.join(env_path, ".env.dev")
    elif environment == 'TESTING':
        env_file = os.path.join(env_path, ".env.test")
    else:
        raise Exception(f"Invalid environment value '{environment}' found! Expected 'PRODUCTION', 'DEVELOPMENT', or 'TESTING'.")
    
    print(f"Loading environment file - {env_file}")
    load_dotenv(env_file)


class Config():
    def __init__(self):
        load_config()


    def get_config_object(self):
        config_object = {
        "SERVER_PORT" : os.environ.get("SERVER_PORT"),
        "SERVER_HOST" : os.environ.get("SERVER_HOST"),
        "ENVIRONMENT": os.environ.get('ENVIRONMENT')
        }

        return config_object
    


