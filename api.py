import requests


def notify(content: str, url: str, uuid: int):
    payload = {
        "text": content,
        "uuid": uuid,
    }
    r = requests.post(url, uuid)


if __name__ == "__main__":
    import toml

    # Load Configurations
    fname = "config.toml"
    with open(fname, "r") as f:
        config = toml.load(f)
    # Telegram settings
    TOKEN = config["token"]
    CHAT_ID = config["chat_id"]
    FLASK_TOKEN = config["flask_token"]

    notify(content="TestTest~", url="http://localhost:5000", uuid=FLASK_TOKEN)
