import os
import yaml
from flask import Flask

# tags yaml

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    print(f"\ninstance_path {app.instance_path}")
    # app.config.from_mapping(
    #     SECRET_KEY='123@#$',
    #     DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    # )
    # if test_config is None:
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     app.config.from_mapping(test_config)

    # try:
    #     print(f"app.instance_path: {app.instance_path}")
    #     os.makedirs(app.instance_path)
    # except OSError as e:
    #     print(f"error: {e}")

    if (app.config["ENV"] == "development"):
        print(f"\napp.env: {app.env}")
        # app.config.update(
        #     TESTING=True,
        #     SECRET_KEY=b'123@#$'
        # )

        ## tags config
        # with app.open_instance_resource('config.yaml') as f:
        #     # cfg2 = f.read()
        #     # print(f"cfg2: {cfg2}")

        #     cfg = yaml.safe_load(f)
        #     print(f"\ncfg: {cfg}")
        #     # for section in cfg:
        #         # print(f"section: {section}")
        #     # cfg[] when no exist key return is Error
        #     # cfg['mariadb']['USER']
        #     # return is None
        #     #cfg.get('mariadb).get('USER')
        #     print(f"\ncfg['DATABASE_USER']: {cfg['DATABASE_USER']}")
        #     print(f"\ncfg['DATABASE_ENGINE']: {cfg['DATABASE_ENGINE']}")
        #     # app.config.from_pyfile(cfg, silent=True)

        yaml_path = os.path.join(app.instance_path, 'config.yaml')
        print(f"\nyaml_path: {yaml_path}")
        #yaml.load --> yaml.safe_load
        app.config.from_file(yaml_path, load=yaml.safe_load)

        # print(f"\napp.database_user: {app.database_user}")
        print(f"\napp.config['DATABASE_USER']: {app.config['DATABASE_USER']}\napp.config['DATABASE_ENGINE']: {app.config['DATABASE_ENGINE']}")
    
    @app.route('/hello')
    def hello():
        
        return 'Hello my friends'
    
    return app