import os
import yaml
from flask import Flask

# tags yaml

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if (app.config["ENV"] == "development"):
        yaml_path = os.path.join(app.instance_path, 'config.yaml')
        #yaml.load --> yaml.safe_load
        app.config.from_file(yaml_path, load=yaml.safe_load)
        print(f"\napp.config['DATABASE_USER']: {app.config['DATABASE_USER']}\napp.config['DATABASE_ENGINE']: {app.config['DATABASE_ENGINE']}")
    
    @app.route('/hello')
    def hello():
        
        return 'Hello my friends'
    
    return app