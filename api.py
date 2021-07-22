import requests
import threading
from icecream import ic

def notify(content: str, url: str, uuid: int, non_block: bool=True):
    # Thread worker
    def f(content: str, url: str, uuid: int):
        payload = {
        "text": content,
        "uuid": uuid,
    }
        r = requests.post(url, json=payload)
        ic(r.response)

    thread = threading.Thread(target=notify, args=(content, url, uuid))
    thread.start()
    
    if not non_block:
        thread.join()
        

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

    notify(content="TestTest~", url="http://localhost:5000/notify", uuid=FLASK_TOKEN)
