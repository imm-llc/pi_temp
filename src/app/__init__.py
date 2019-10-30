from flask import Flask

app = Flask("pi_temp")

app.config.from_envvar('PI_TEMP_APP_SETTINGS')

with app.app_context():

    from app import routes


if __name__ == "__main__":
    app.run(host='0.0.0.0')